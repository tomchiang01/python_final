import tkinter as tk
from Widget_Window import Widget_Window

def main(): 
    root = tk.Tk()
    widget = Widget_Window(root)
    root.mainloop()
    widget.kill()

if __name__ == '__main__':
    main()