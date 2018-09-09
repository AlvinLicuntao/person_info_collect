from tkinter import Menu, messagebox
from .home.HomeView import HomeView


class AUIMenu(Menu):
    def __init__(self, win):
        super(AUIMenu, self).__init__(win)
        win.config(menu=self)
        # home menu
        home = Menu(self, tearoff=0)
        home.add_command(label='View', command=self._home_menu_view)
        home.add_command(label='Manage', command=self._home_menu_manage)
        home.add_command(label='Graphic', command=self._home_menu_graphic)
        self.add_cascade(label='Home', menu=home)
        self.ui_view = HomeView(win)
        self.ui_view.grid(column=0, row=0)

        # spider menu
        self.add_cascade(label='Spider', command=self._spider_menu)
        # message menu
        message = Menu(self, tearoff=0)
        message.add_command(label='info', command=self._message_info)
        message.add_command(label='warning', command=self._message_warning)
        message.add_command(label='error', command=self._message_error)
        message.add_separator()
        message.add_command(label='confirm', command=self._message_confirm)
        self.add_cascade(label='Message', menu=message)

    # spider menu command
    def _spider_menu(self):
        print('spider menu choose')

    # home menu command
    def _home_menu_view(self):
        print('_home_menu_view choose')

    def _home_menu_manage(self):
        print('_home_menu_manage choose')

    def _home_menu_graphic(self):
        print('_home_menu_graphic choose')

    # message menu command
    def _message_info(self):
        messagebox.showinfo('Python message info box',
                            'This Application created to note my tecology:\n Date: 2018-08-06')

    def _message_warning(self):
        messagebox.showwarning('Python message info box',
                               'This Application created to note my tecology:\n Date: 2018-08-06')

    def _message_error(self):
        messagebox.showerror('Python message info box',
                             'This Application created to note my tecology:\n Date: 2018-08-06')

    def _message_confirm(self):
        answer = messagebox.askyesno('Python message info box',
                                     'This Application created to note my tecology:\n Date: 2018-08-06')
        print('answer is: {}'.format(answer))
