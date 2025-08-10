##################################################
# RansackIt
#
# Written by Jacob Adams 
##################################################



##################################################
# Module imports
##################################################
import tkinter as tk
import game
import math

APP_NAME = "RansackIt"
VERSION = "1.0.0"

##################################################
# Base Clases
##################################################
class BaseFrame(tk.Frame):
    """An abstract base class for the frames that sit inside PythonGUI.

    Args:
      master (tk.Frame): The parent widget.
      controller (PythonGUI): The controlling Tk object.

    Attributes:
      controller (PythonGUI): The controlling Tk object.

    """

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the frame."""
        raise NotImplementedError

class GameFrame(BaseFrame):
    #Create the base widgets for the frame.
    def create_widgets(self):
        # Configure 3 columns
        my_game = game.Game(self)

        my_game.start_game()
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        my_game.canvas.grid(row=0, column=0, sticky="nsew")
        



class MainMenu(BaseFrame):
    #Create the base widgets for the frame.
    def create_widgets(self):
        # Configure 3 columns

        self.new_button = tk.Button(self,
                                    anchor='center',
                                    command=lambda: self.controller.show_frame(GameFrame),
                                    padx=5,
                                    pady=5,
                                    text="Play Game")
        self.new_button.grid(padx=5, pady=5)


class App(tk.Tk):
    """The main window of the GUI.

    Attributes:
      container (tk.Frame): The frame container for the sub-frames.
      frames (dict of tk.Frame): The available sub-frames.

    """

    def __init__(self):
        tk.Tk.__init__(self)
        self.title(f"{APP_NAME} V{VERSION}")
        self.center_window()
        self.create_widgets()
        self.resizable(0, 0)

    def create_widgets(self):
        """Create the widgets for the frame."""             
        #   Frame Container
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        #label = tk.Label(self.container, text="Hello, this is some text!", font=("Arial", 14))
        #label.grid(row=0, column=1, sticky="nsew")

        #   Frames
        self.frames = {}
        for f in (MainMenu, GameFrame): # defined subclasses of BaseFrame
            frame = f(self.container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[f] = frame
        self.show_frame(MainMenu)

    def show_frame(self, cls):
        self.frames[cls].tkraise()

    def center_window(self):
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate 50% dimensions
        width = int(screen_width * 0.75)
        height = int(screen_height * 0.75)

        # Calculate position to center the window
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Set window size and position
        self.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
    exit()