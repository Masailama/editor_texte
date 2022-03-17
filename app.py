import tkinter as tk
from editor import Editor
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
        self.editor = Editor(self)
        self.bind_functions()

    def bind_functions(self):
        self.bind("<Control-q>", lambda _: self.destroy())
        self.bind("<Control-n>", lambda _:self.add_file())
        self.bind("<Control-o>", lambda _:self.open_file())
        self.bind("<Control-r>", lambda _:self.run_file())
    
    def add_file(self):
        self.file_list.add_file()
    
    def open_file(self):
        self.file_list.open_file()
    
    def run_file(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()