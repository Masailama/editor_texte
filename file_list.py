import tkinter as tk
from tkinter import filedialog
from editor import Editor
from utils import BACK_FILES, FOREGROUND, PATH_ADD, PATH_OPEN, PATH_RUN, PATH_SAVE, PATH_SAVE_AS


class FileList(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window, bg=BACK_FILES)
        self.img_add = tk.PhotoImage(file=PATH_ADD)
        self.img_run = tk.PhotoImage(file=PATH_RUN)
        self.img_open = tk.PhotoImage(file=PATH_OPEN)
        self.img_save = tk.PhotoImage(file=PATH_SAVE)
        self.img_save_as = tk.PhotoImage(file=PATH_SAVE_AS)
        self.path_files = []
        self.frame_buttons = tk.Frame(self, bg=BACK_FILES)
        self.lb_add = tk.Label(self.frame_buttons, image=self.img_add, bg=BACK_FILES, fg=FOREGROUND)
        self.lb_open = tk.Label(self.frame_buttons, image=self.img_open, bg=BACK_FILES, fg=FOREGROUND)
        self.lb_save = tk.Label(self.frame_buttons, image=self.img_save, bg=BACK_FILES, fg=FOREGROUND)
        self.lb_save_as = tk.Label(self.frame_buttons, image=self.img_save_as, bg=BACK_FILES, fg=FOREGROUND)
        self.lb_run = tk.Label(self.frame_buttons, image=self.img_run, bg=BACK_FILES, fg=FOREGROUND)
        self.frame_list = tk.Frame(self, bg=BACK_FILES)
        self.lb_files = tk.Label(self.frame_list, text="Files", bg=self.cget("bg"), fg=FOREGROUND)
        self.list = tk.Listbox(self.frame_list, bg=self.cget("bg"), fg=FOREGROUND, bd=0, relief="flat", 
            highlightthickness=0)
        self.draw()
        self.bind_functions()
        self.editor = Editor(window)
        
    def draw(self):
        self.pack(side="left", fill=tk.Y, anchor="w")
        self.frame_buttons.pack(side="left", fill=tk.Y)
        self.lb_add.grid(row=0, column=0, pady=(10, 0))
        self.lb_open.grid(row=1, column=0, pady=(10, 0))
        self.lb_save.grid(row=2, column=0, pady=(10, 0))
        self.lb_save_as.grid(row=3, column=0, pady=(10, 0))
        self.lb_run.grid(row=4, column=0, pady=(10, 0))
        self.frame_list.pack(side="right", fill=tk.Y)
        self.lb_files.pack(fill=tk.X, pady=5)
        self.list.pack(fill=tk.BOTH, expand=True, padx=20)

    def bind_functions(self):
        self.lb_add.bind("<Button-1>", lambda _: self.add_file())
        self.lb_open.bind("<Button-1>", lambda _: self.open_file())
        self.lb_run.bind("<Button-1>", lambda _: self.run_file())
        self.list.bind("<Double Button-1>", lambda _: self.select_file_list())

    def add_file(self):
        item = filedialog.asksaveasfile(title="Nou arxiu", filetypes=(("Python files", "*.py"),), 
            defaultextension=((".py"),))
        if item:
            self.path_files.append(item.name)
            self.fill_list(item.name)
            self.editor.editor.focus_set()

    def open_file(self):
        item = filedialog.askopenfilename(title="Obrir arxiu", filetypes=(("Python files", "*.py"),))
        if item:
            self.path_files.append(item)
            self.fill_list(item)
            self.editor.load_file(item)
            self.editor.editor.focus_set()

    def save_file(self):
        pass

    def save_as_file(self):
        filedialog.asksaveasfile(title="Guardar com", filetypes=(("Python files", "*.py"),), 
            defaultextension=((".py")))


    def run_file(self):
        self.editor.run_file()

    def fill_list(self, item):
        self.list.insert(tk.END, item.split("/")[-1])
        num = int(self.list.index(tk.END)) - 1
        self.list.select_clear(0, tk.END)
        self.list.select_set(self.list.index(num))

    def select_file_list(self):
        self.editor.load_file(self.path_files[self.list.curselection()[0]])