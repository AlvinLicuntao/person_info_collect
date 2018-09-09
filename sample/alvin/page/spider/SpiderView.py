from tkinter import ttk
import tkinter as tk


class AUISpiderView(object):
    def __init__(self, win):
        super(AUISpiderView, self).__init__(win)
        tab = ttk.Notebook(win)
        tab1 = ttk.Frame(tab)
        tab2 = ttk.Frame(tab)
        tab.add(tab1, text='Tab 01')
        tab.add(tab2, text='Tab 02')

        ttk.Label(tab1, text='Tab 01 content is here').grid(column=0, row=0, sticky='W')
        ttk.Label(tab2, text='Tab 02 content is here').grid(column=0, row=0, sticky='W')
        # ttk.Label(tab2,text='Tab 02 content is here').grid(column=0,row=0,sticky='W')
        tab.grid(column=0, row=0)
