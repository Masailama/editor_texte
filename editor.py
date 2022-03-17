import tkinter as tk
from tkinter import ttk
from utils import BACKGROUND, FOREGROUND


class Editor(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window, bg=BACKGROUND)
        self.editor = tk.Text(self, height=32, bg=BACKGROUND, bd=0, relief="flat", fg=FOREGROUND, 
            highlightthickness=0, insertbackground="white")
        self.terminal = tk.Text(self, bg=BACKGROUND, bd=0, relief="flat", fg=FOREGROUND, highlightthickness=0)
        self.draw()

    def draw(self):
        self.pack(fill=tk.BOTH, expand=True, anchor="e")
        self.editor.pack(fill=tk.X)
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.X)
        self.terminal.pack(fill=tk.BOTH)

    def run_file(self):
        print("run file")

    def load_file(self, path_file):
        self.editor.delete(1.0, tk.END)
        f = open(path_file)
        self.editor.insert(1.0, f.read())
        f.close()
