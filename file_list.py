import tkinter as tk
from tkinter import filedialog
from utils import BACK_FILES, FOREGROUND, PATH_ADD, PATH_OPEN, PATH_RUN


class FileList(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window, bg=BACK_FILES)
        self.img_add = tk.PhotoImage(file=PATH_ADD)
        self.img_run = tk.PhotoImage(file=PATH_RUN)
        self.img_open = tk.PhotoImage(file=PATH_OPEN)
        self.frame_buttons = tk.Frame(self, bg=BACK_FILES)
        self.lb_add = tk.Label(self.frame_buttons, image=self.img_add, bg=BACK_FILES, fg=FOREGROUND, 
            text="Nou", compound="top")
        self.lb_open = tk.Label(self.frame_buttons, image=self.img_open, bg=BACK_FILES, fg=FOREGROUND, 
            text="Obrir", compound="top")
        self.lb_run = tk.Label(self.frame_buttons, image=self.img_run, bg=BACK_FILES, fg=FOREGROUND, 
            text="Executar", compound="top")
        self.frame_list = tk.Frame(self, bg=BACK_FILES)
        self.list = tk.Listbox(self.frame_list, bg=self.cget("bg"), bd=0, relief="flat",highlightthickness=0)
        self.draw()
        self.bind_functions()
        
    def draw(self):
        self.pack(side="left", fill=tk.Y, anchor="w")
        self.frame_buttons.pack()
        self.lb_add.grid(row=0, column=0, padx=10, pady=5)
        self.lb_open.grid(row=0, column=1, padx=10, pady=5)
        self.lb_run.grid(row=0, column=2, padx=10, pady=5)
        self.frame_list.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self.list.pack(fill=tk.BOTH, expand=True)

    def bind_functions(self):
        self.lb_add.bind("<Button-1>", lambda _: self.add_file())
        self.lb_open.bind("<Button-1>", lambda _: self.open_file())
        self.lb_run.bind("<Button-1>", lambda _: self.run_file())

    def add_file(self):
        item = filedialog.asksaveasfile(title="Nou arxiu", filetypes=(("Python files", "*.py"),), 
            defaultextension=((".py"),))
        if item:
            print(item.name)

    def open_file(self):
        item = filedialog.askopenfilename(title="Obrir arxiu", filetypes=(("Python files", "*.py"),))
        if item:
            print(item)

    def run_file(self):
        pass