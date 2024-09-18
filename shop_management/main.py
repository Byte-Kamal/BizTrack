# pylint: disable=missing-docstring


import tkinter as tk

from shop_gui import ShopGUI

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = ShopGUI(root)
        root.mainloop()
    except tk.TclError as e:
        print(f"A Tkinter error occurred: {e}")
    except ImportError as e:
        print(f"An import error occurred: {e}")
