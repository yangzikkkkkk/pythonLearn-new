import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([5, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6])
y = np.array([0.98, 0.92, 0.88, 0.85, 0.8, 0.78,0.75, 0.71, 0.69, 0.66, 0.62, 0.6, 0.57, 0.54, 0.5 ])

plt.figure(num="OTA和入住率的关系预测")
plt.scatter(x,y)
plt.show()

model = LinearRegression()
model.fit(x.reshape(-1,1), y)
y_pred = model.predict([[5]])

# 计算 R2 值
r2 = model.score(x.reshape(-1,1), y)
print('R2 值：', r2)
print(y_pred)
