import tkinter as tk
from gui import FileSystemGUI


if __name__ == "__main__":
    root_dir = tk.Tk()
    app = FileSystemGUI(root_dir)
    root_dir.mainloop()
