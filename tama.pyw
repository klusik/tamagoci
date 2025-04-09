"""
    Tamagoči for a friend :-)

    Author: Rudolf Klusal
    Licence: Probably BSD, we'll see :-P Surely not GNU/GPL :-P
"""

# MAIN IMPORTS #

# LOCAL IMPORTS #
from src.window import Window

# CLASSES #
class App:
    def __init__(self):
        self.window = Window()

    def run(self) -> None:
        """
        Run the app
        :return: None
        """
        self.window.run()


# RUNTIME #
if __name__ == "__main__":
    app = App()
    app.run()