import tkinter as tk
import os
from tkinter import Frame
from .Menu import AUIMenu
from .login.Login import AUILogin


class Index(Frame):
    def __init__(self, config):
        self.config = config
        self.window = tk.Tk()
        self.window.title(self.config.get('app', 'name'))
        # 渲染登陆组件，并监听登陆完成事件
        # self.children = AUILogin(self.window, self.config).on('success', self.login_success)

        # 渲染内容
        self.children = AUIMenu(self.window)

        self.window.iconbitmap(os.getcwd() + self.config.get('app', 'icon'))
        self.window.mainloop()

    def login_success(self, data):
        self.children.destroy()
        self.children = AUIMenu(self.window)
