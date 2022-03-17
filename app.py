import tkinter as tk
from file_list import FileList


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de texte")
        try:
            self.attributes("-zoomed", True)
            self.bind("<F11>", lambda _: self.attributes("-zoomed", not self.attributes("-zoomed")))
        except:
            self.attributes("-fullscreen", True)
            self.bind("<F11>", lambda _: self.attributes("-fullscreen", not self.attributes("-fullscreen")))
        self.file_list = FileList(self)
        self.bind_functions()

    def bind_functions(self):
        self.bind("<Control-q>", lambda _: self.destroy())
        self.bind("<Control-n>", lambda _: self.add_file())
        self.bind("<Control-s>", lambda _: self.save_file())
        self.bind("<Control-Shift-S>", lambda _: self.save_as_file())
        self.bind("<Control-o>", lambda _: self.open_file())
        self.bind("<Control-r>", lambda _: self.run_file())
    
    def add_file(self):
        self.file_list.add_file()
    
    def open_file(self):
        self.file_list.open_file()

    def save_file(self):
        self.file_list.save_file()
    
    def save_as_file(self):
        self.file_list.save_as_file()

    def run_file(self):
        self.file_list.run_file()


if __name__ == "__main__":
    app = App()
    app.mainloop()