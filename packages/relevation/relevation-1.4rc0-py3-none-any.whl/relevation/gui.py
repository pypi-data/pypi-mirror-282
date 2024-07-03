#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Relevation Password Printer
a command line interface to Revelation Password Manager.

Simplistic Graphical User Interface.
This GUI is mainly intended to be used in systems where command-lines
are less common, like Windows.

$Id$
"""
# Relevation Password Printer
#
# Copyright (c) 2011, 2013, 2024 Toni Corvera
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
try:
    # tkinter is standard module but some distributions drop it by default and e.g. it is optional on Windows
    import tkinter as tk
except ImportError:
    print('The Tkinter module is not available in your Python installation, can\'t continue', file=sys.stderr)
    sys.exit(1)
from tkinter import Frame, Button, Entry, Listbox, Scrollbar, Radiobutton, StringVar

from . import __main__ as rlv
from . import __author__, __version__

__date__ = '$Date$'
__revision__ = '$Rev$'

old_fn = rlv.dump_result

def append_result(typeName, name, descr, notes, fields):
    global gui
    gui.lst.insert(tk.END, name)
    s = '\n'
    s += 'Type: %s\n' % typeName
    s += 'Name: %s\n' % name
    s += 'Description: %s\n' % descr
    s += 'Notes: %s\n' % notes
    for field in fields:
        s += '%s %s\n' % field
    gui.items.append(s)

def dump_result_override(res, query_desc):
    return old_fn(res, query_desc, append_result)

rlv.dump_result = dump_result_override

class ResultDialog:
    def __init__(self, parent, result):
        top = self.top = tk.Toplevel(parent)

        self.value = tk.Text(top)
        self.value.insert(tk.END, result)
        self.value.config(state=tk.DISABLED)
        self.value.pack()
        b = Button(top, text='OK', command=self.ok)
        b.pack(pady=5)

        top.bind('<Return>', lambda event: self.ok())
        top.focus_set()

    def ok(self):
        self.top.destroy()

class GUI(object):
    def do_find(self):
        global rootw
        search = self.search_text.get()
        self.lst.delete(0, tk.END)
        self.items = []
        mode = '-O'
        args = sys.argv[1:] + [ '-s', ]
        if self.mode.get() == rlv.MODE_AND:
            mode = '-A'
            search = search.split(' ')
            args += search
            args += [ mode, ]
        else:
            args += [ search, mode ]
        print(args)
        try:
            rlv.main(args)
        except SystemExit:
            # No matches -> Exit with 80
            gui.lst.insert(tk.END, '<No matches>')
            self.items.append('<No passwords matched search>')

    def display(self):
        global rootw
        selected = self.lst.curselection()
        if not selected:
            return
        selected = int(selected[0])
        item = self.items[selected]
        print(item)
        dlg = ResultDialog(rootw, item)
        rootw.wait_window(dlg.top)

    def __init__(self, master=None):
        self.master = master
        frame = Frame(master)
        frame.pack(expand=1, fill=tk.BOTH)
        self.items = []
        self.frame = frame
        #top = master
        top = frame.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1, pad=5)
        frame.rowconfigure(0, weight=1, pad=5)
        frame.columnconfigure(0, weight=1)

        # Avoid printing to stderr
        def ignoreme(s):
            pass
        rlv.printe = ignoreme
        
        FILL = tk.N+tk.S+tk.E+tk.W
        BTNROW = 3
        MODEROW = 2
        RESROW = 1
        # Populate
        self.search_text = Entry(self.frame)
        #self.search_text.pack({'expand': 1, 'side': 'top'})
        self.search_text.grid(row=0, column=0, columnspan=4, padx=5, sticky=tk.N+tk.E+tk.W)
        self.search_text.bind('<Return>', lambda event: self.do_find())
        
        self.quit = Button(self.frame, text='Quit', fg='red', command=frame.quit)
        #self.quit.pack(side=tk.LEFT)
        self.quit.grid(row=BTNROW, column=0, padx=10)
        
        self.search = Button(self.frame, text='Search', command=self.do_find)
        #self.search.pack(side=tk.RIGHT)
        self.search.grid(row=BTNROW, column=2, padx=5)

        self.mode = StringVar()

        mode = rlv.load_config()[2]
        self.mode.set(mode)

        rbO = Radiobutton(self.frame, text="OR/Literal", variable=self.mode, value=rlv.MODE_OR)
        rbA = Radiobutton(self.frame, text="AND", variable=self.mode, value=rlv.MODE_AND)
        rbO.grid(row=MODEROW, column=0)
        rbA.grid(row=MODEROW, column=1)
        
        self.view = Button(self.frame, text='View', command=self.display)
        #self.view.pack(side=tk.RIGHT)
        self.view.grid(row=BTNROW, column=1)

        ## FIXME
        scrollbar = Scrollbar(self.frame, orient=tk.VERTICAL)
        scrollbar.grid(row=RESROW, column=4, sticky=FILL)
        
        self.lst = Listbox(self.frame)
        #self.lst.pack()
        self.lst.grid(row=RESROW, column=0, columnspan=3, sticky=FILL)
        self.lst.bind('<Double-Button-1>', lambda event: self.display())

        self.lst.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lst.yview)

        self.search_text.focus_set()

def entrypoint():
    global gui
    rootw = tk.Tk()
    rootw.title('Relevation search v' + __version__)
    gui = GUI(master=rootw)
    rootw.mainloop()
    #rootw.destroy()

if __name__ == '__main__':
    entrypoint()

# vim:set ts=4 et ai fileencoding=utf-8: #
