"""
- will allow user to dynamically switch between basic ui and scientific ui without having
to switch between two applications
"""

import tkinter as tk
from window import *
import basic_ui
import scientific_ui
import unit_converter_gui
#window = tk.Tk()
#window.resizable(width=False, height=False)
#window_type = ["Basic", "Scientific", "Unit Converter"]
#window.mainloop()

#from basic_ui import basic_frm
#from scientific_ui import scientific_frm
#from unit_converter_gui import unit_conv_master_frm
#from window import *
#window_type = ["Basic", "Scientific", "Unit Converter"]
#window = tk.Tk()
#window.resizable(width=False, height=False)


#ui = window_type[0]
def main():
    ui = window_type[0]
    dropdown_frm = tk.Frame(master=window)
    dropdown_frm.grid(row=0, column=0, pady=10, sticky="w")
    window_type_clicked = tk.StringVar()
    window_type_dropdown = tk.OptionMenu(dropdown_frm, window_type_clicked, *window_type)
    window_type_dropdown.grid(row=0, column=0, padx=10)
    while ui != "Exit":
        #window = tk.Tk()
        #dropdown_frm = tk.Frame(master=window)
        #dropdown_frm.grid(row=0, column=0, pady=10, sticky="w")
        #window_type_clicked = tk.StringVar()
        window_type_clicked.set(ui)
        #window_type_dropdown = tk.OptionMenu(dropdown_frm, window_type_clicked, *window_type)
        #window_type_dropdown.grid(row=0, column=0, padx=10)
        if window_type_clicked.get() == "Basic":
            #from basic_ui import basic_frm
            ui_frm = basic_ui.basic_frm
        elif window_type_clicked.get() == "Scientific":
            #from scientific_ui import scientific_frm
            ui_frm = scientific_ui.scientific_frm
        elif window_type_clicked.get() == "Unit Converter":
            #from unit_converter_gui import unit_conv_master_frm
            ui_frm = unit_converter_gui.unit_conv_master_frm
        ui_frm.grid(row=1, column=0, pady=5)
        window.title("CalcX - " + ui)
        while ui == window_type_clicked.get():
            window.update_idletasks()
            window.update()
        ui_frm.grid_forget()
        ui = window_type_clicked.get()

        

    
