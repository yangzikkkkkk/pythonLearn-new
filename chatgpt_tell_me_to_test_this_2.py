import tkinter as tk

def run_program():
    # 这里可以写你需要执行的程序
    # 比如输入一个参数 lambda 并计算出结果
    lambda = lambda**2
    return lambda

def create_dialog():
    # 创建对话框窗口
    dialog = tk.Toplevel()

    # 添加输入框和标签
    label = tk.Label(dialog, text="请输入参数 lambda:")
    label.pack()
    entry = tk.Entry(dialog)
    entry.pack()

    # 添加确认按钮
    button = tk.Button(dialog, text="确认", command=lambda: [dialog.destroy(), run_program(entry.get())])
    button.pack()

    # 显示对话框
    dialog.mainloop()

# 运行程序
create_dialog()
