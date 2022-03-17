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


if __name__ == "__main__":
    app = App()
    app.mainloop()