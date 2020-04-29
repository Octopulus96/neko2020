import os
import sys
import tkinter as tk
from infi.systray import SysTrayIcon
from neko2020 import neko
from neko2020.utils import files, images


def timer(root, myNeko):

    myNeko.update()
    root.after(200, lambda: timer(root, myNeko))


def onclicked(root):
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    canvas = tk.Canvas(bg="green", width=w, height=h, highlightthickness=0)
    canvas.place(x=0, y=0)
    root.overrideredirect(True)
    root.geometry(f"{w}x{h}+0+0")
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "green")

    myNeko = neko.Neko(canvas)

    def hello(systray):
        print("hello")

    def quit(systray):
        root.quit()

    with SysTrayIcon(
        os.path.join(files.get_project_root(), "resource", "neko", "Awake.ico"),
        "Neko",
        set(),
        on_quit=quit,
    ):
        timer(root, myNeko)
        root.mainloop()
