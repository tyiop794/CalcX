import tkinter as tk
#import main

window = tk.Tk()
window.resizable(width=False, height=False)
window_type = ["Basic", "Scientific", "Unit Converter", "Exit"]
from main import main
main()
#window.mainloop()
