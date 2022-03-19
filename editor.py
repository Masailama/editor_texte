import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils import BACKGROUND, FOREGROUND


class Editor(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window, bg=BACKGROUND)
        self.editor = tk.Text(self, height=32, bg=BACKGROUND, bd=0, relief="flat", fg=FOREGROUND, 
            highlightthickness=0, insertbackground="white")
        self.output = tk.Text(self, bg=BACKGROUND, bd=0, relief="flat", fg=FOREGROUND, highlightthickness=0)
        self.draw()

    def draw(self):
        self.pack(fill=tk.BOTH, expand=True, anchor="e")
        self.editor.pack(fill=tk.X)
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.X)
        self.output.pack(fill=tk.BOTH)

    def save_file(self, path_file=None):
        if path_file == None:
            messagebox.showerror("Error", "Has de seleccionar un arxiu.")
            return
        f = open(path_file, "w")
        f.write(self.editor.get(1.0, tk.END))
        f.close()
        messagebox.showinfo("Guardar", "Arxiu guardat satisfactoriament.")

    def run_file(self, path_file=None):
        if path_file == None:
            messagebox.showerror("Error", "Has de guardar l'arxiu abans de executar-lo.")
            return
        command = f"python3 {path_file}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        self.output.delete(1.0, tk.END)
        self.output.insert(1.0, output)
        self.output.insert(1.0, error)

    def load_file(self, path_file=None):
        self.editor.delete(1.0, tk.END)
        f = open(path_file)
        self.editor.insert(1.0, f.read())
        f.close()
