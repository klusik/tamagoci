"""
    Window handler

    Author: Rudolf Klusal
"""
# IMPORTS #
import tkinter as tk

# CLASSES #
class Window:
    def __init__(self,
                 title: str="Tamagochi game for a friend",
                 width: int=600,
                 height: int=400,
                 ):
        self.root = tk.Tk()
        self.root.title = title

        self.container: tk.Frame = tk.Frame(
            self.root,
            width=width,
            height=height,
        )
        self.container.pack(fill=tk.BOTH, expand=True)

    def get_container(self) -> tk.Frame:
        """
        Getting the container
        :return: the container
        :rtype: tk.Frame
        """
        return self.container

    def run(self) -> None:
        """
        Make the window
        :return: None
        """
        self.root.mainloop()