from tkinter import ttk, font, E, W
from .Search import Search


class HomeView(ttk.Frame):
    def __init__(self, win):
        super(HomeView, self).__init__(win)

        self.ui_title = ttk.Label(self, text="家庭成员列表", font=font.Font(size=18, weight="bold"))
        self.ui_title.grid(column=0, row=0, padx=100, pady=10, columnspan=2)

        self.ui_search = Search(self)
        self.ui_search.grid(column=0, row=1, padx=20, pady=10, columnspan=2)
        self.ui_search.on('choose', lambda e: self._person_detail(e.get('data')))

        self.ui_view = ttk.Button(self, text='查看', command=self._person_detail)
        self.ui_view.grid(column=1, row=2, sticky=W, padx=20, pady='0 20')
        self.ui_edit = ttk.Button(self, text='编辑', command=self._person_edit)
        self.ui_edit.grid(column=0, row=2, sticky=E, padx=20, pady='0 20')

    def _person_detail(self, data=None):
        if not data:
            data = self.ui_search.get_person()
        print(data)

    def _person_edit(self):
        data = self.ui_search.get_person()
        print(data)
