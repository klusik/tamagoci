"""
    Window handler

    Author: Rudolf Klusal
"""
# IMPORTS #
import tkinter as tk

# CLASSES #
class Window:
    def __init__(self,
                 title="Tamagochi game for a friend",
                 width=600,
                 height=400,
                 ):
        self.root = tk.Tk()
        self.root.title = title

        self.container = tk.Frame(
            self.root,
            width=width,
            height=height,
        )
        self.container.pack(fill=tk.BOTH, expand=True)

    def get_container(self):
        return self.container

    def run(self):
        self.root.mainloop()