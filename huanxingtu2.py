import pandas as pd
import plotly.graph_objects as go
import matplotlib.cm as cm
import numpy as np

# Load the data
file_path = "/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/22 UP预售工作/104 新版HDOS+UP的素材整理/（英文版）modified_五星级酒店的结构.xlsx"
df = pd.read_excel(file_path)




# Load the data

# Forward fill the NaN values
df.fillna(method='ffill', inplace=True)

# Create a separate data frame for each level
df_departments = pd.DataFrame(df['Department'].unique(), columns=['name'])
df_departments['parent'] = ''

df_positions = df[['Department', 'Positions']].drop_duplicates()
df_positions.columns = ['parent', 'name']

df_duties = df[['Positions', 'Main Responsibilities']].drop_duplicates()
df_duties.columns = ['parent', 'name']

# Sort departments starting with "Reception Department" or any other starting point
start_department = "Reception Department" # Change this to the correct department name if needed
sorted_departments = df_departments['name'].tolist()
sorted_departments.sort(key=lambda x: (x != start_department, x))  # this will put the starting department at the beginning and sort the rest alphabetically
df_departments = df_departments.set_index('name').loc[sorted_departments].reset_index()

# Assign a color to each department
colors = cm.get_cmap('Blues', len(df_departments))  # use the whole colormap to get a full range of blues
department_colors = {department: 'rgb'+str(tuple(np.array(colors((i+1)/len(df_departments))[:3])*255)) for i, department in enumerate(df_departments['name'])}  # use the sorted order of departments and multiply by 255 to get RGB values

# Assign colors to all rows based on their department
df_departments['color'] = df_departments['name'].map(department_colors)
df_positions['color'] = df_positions['parent'].map(department_colors)
df_duties['color'] = df_duties['parent'].map(department_colors)

# Concatenate all data frames
df_all = pd.concat([df_departments, df_positions, df_duties])

# Create the sunburst chart
fig = go.Figure(go.Sunburst(
    labels=df_all['name'],
    parents=df_all['parent'],
    marker=dict(
        colors=df_all['color'],
    ),
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()
