import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from PIL import ImageTk

word_query = {
    0: "我喜欢你！",
    1: "我养你！",
    2: "我养你呀！",
    3: "我爱你！",
    4: "可以做我的女朋友吗！",
    5: "不想错过你！",
    6: "我陪你！",
}


class Love:
    def __init__(self):
        self.root = tk.Tk()
        self.confirm = ttk.Button()  # 确认按钮
        self.label_pic = ttk.Label()  # 图片
        self.photo = ImageTk.PhotoImage(file="./pictureset/1.gif")  # 显示图片
        self.text = ttk.Label()  # 显示

    def ensure(self, result=False):
        while not result:
            result = messagebox.askyesno("嗯", word_query[random.randrange(len(word_query))])
            if not result:
                messagebox.showinfo("tip", "给个机会呗！再想想")
        messagebox.showinfo("恭喜你!", "你有一个爱你的男朋友了！")

    def components(self):
        # 距离
        constant_x = 10
        constant_y = 400
        # 组件
        self.text = ttk.Label(self.root, text="我喜欢你！天豪！", width=200).place(x=10, y=10)  # 显示
        self.label_pic = ttk.Label(self.root, image=self.photo).place(x=constant_x + 200, y=10)  # 图片
        self.confirm = ttk.Button(self.root, text="确定", command=self.ensure).place(x=constant_x, y=constant_y)  # 按钮

    def start(self):
        self.root.geometry("750x525+250+100")
        self.components()
        self.root.mainloop()


if __name__ == '__main__':
    love = Love()
    love.start()
