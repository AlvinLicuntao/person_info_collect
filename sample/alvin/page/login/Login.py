import tkinter as tk
from PIL import ImageTk, Image
import os, logging
from tkinter import messagebox as MessageBox, ttk, font, PhotoImage
from ..mixin.Emitter import Emitter


class AUILogin(Emitter, ttk.Frame):
    def __init__(self, win, config):
        super(AUILogin, self).__init__(win, width=800, height=600)
        self.config = config
        self.grid(column=0, row=0, padx=100, pady=20)
        title = ttk.Label(self, text="Login", font=font.Font(size=32, weight="bold"))
        title.grid(column=0, row=0, columnspan=3, pady=8)

        ttk.Label(self,
                  image=ImageTk.PhotoImage(Image.open(os.getcwd() + self.config.get('app', 'preview')))).grid(column=0,
                                                                                                              row=1,
                                                                                                              columnspan=3)

        name = tk.StringVar()
        nameInput = ttk.Entry(self, textvariable=name)
        nameInput.grid(column=1, row=2, padx=8, pady=4, sticky='w')
        nameInput.focus()

        nameLabel = ttk.Label(self, text="Username:")
        nameLabel.grid(column=0, row=2, padx=8, pady=4, sticky='e')

        pwd = tk.StringVar()
        pwdInput = ttk.Entry(self, textvariable=pwd, show='*')
        pwdInput.grid(column=1, row=3, padx=8, pady=4, sticky='w')

        pwdLabel = ttk.Label(self, text="Password:")
        pwdLabel.grid(column=0, row=3, padx=8, pady=4, sticky='e')

        btnLogin = ttk.Button(self, text="Login", command=lambda: self._login_action(name.get(), pwd.get()))
        btnLogin.grid(column=1, row=4, padx=8, pady=4)

    def _login_action(self, name, pwd):
        if name == pwd:
            logging.info('login success {}'.format(name))
            self._emit('success', {'username': name, 'password': pwd})
        else:
            logging.info('login failed {}'.format(name))
            MessageBox.showwarning('Warning', 'username and password not correct!')
