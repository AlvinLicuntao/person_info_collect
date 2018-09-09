from tkinter import ttk, Toplevel, StringVar, N, W, S, E, Tk, Scrollbar, CENTER
from ..mixin.Emitter import Emitter


class Search(ttk.Frame, Emitter):
    def __init__(self, parent):
        super(Search, self).__init__(parent)
        self._init_search_input()
        self._init_tree()

    def _init_search_input(self):
        # search input label
        self.ui_name_var = StringVar()
        self.ui_name_entry = ttk.Entry(self, textvariable=self.ui_name_var)
        self.ui_name_entry.grid(column=0, row=0, sticky=(W, E))

        self.ui_search_btn = ttk.Button(self, text='Search', command=self._filter_data)
        self.ui_search_btn.grid(column=1, row=0, sticky=W)
        # default status
        self.ui_name_entry.focus()
        # event bindings
        self.ui_search_btn.bind('<Return>', self._filter_data)
        self.ui_name_entry.bind('<Return>', self._filter_data)

    def _init_tree(self):
        trees = ("Name", "Birth", "Death", "Address")
        self.tree = ttk.Treeview(self, show='headings', selectmode='browse', columns=trees)
        self.scrollbar = Scrollbar(self, width=20, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        for c in trees:
            self.tree.column(c, width=100, anchor=CENTER)
            self.tree.heading(c, text=c)

        self._set_tree_data([x for x in range(0, 20)])

        self.tree.grid(column=0, row=1, columnspan=2, sticky=(W, E))
        self.scrollbar.grid(column=4, row=1, sticky=(W, N, S))

        self.tree.bind('<Double-Button-1>', lambda e: self._emit('choose', self.get_person()))
        self.tree.bind('<Return>', lambda e: self._emit('choose', self.get_person()))

    def get_person(self):
        return self.tree.item(self.tree.selection()).get('values')

    def _set_tree_data(self, data):
        for i in data:
            self.tree.insert('', i, values=(i, "Best", i, i))

    # event handler to response search operation
    def _filter_data(self, event=None):
        param = self.ui_name_var.get()
        items = self.tree.get_children()
        self.tree.delete(*items)
        data = []
        for d in range(0, 20):
            if param in str(d):
                data.append(d)
        self._set_tree_data(data)


class SearchModel(Toplevel, Emitter):
    def __init__(self):
        super(SearchModel, self).__init__()
        self.title('Search')
        Search(self).grid(column=0, row=0)


if __name__ == '__main__':
    win = Tk()
    Search(win).grid(column=0, row=0)
    win.title(__file__)
    win.mainloop()
