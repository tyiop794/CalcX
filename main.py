"""
- will allow user to dynamically switch between basic ui and scientific ui without having
to switch between two applications
"""

import tkinter as tk
import basic_ui
import scientific_ui
import unit_converter_gui
window_type = ["Basic", "Scientific", "Unit Converter"]

ui = window_type[0]
def main():
    window = tk.Tk()
    dropdown_frm = tk.Frame(master=window)
    dropdown_frm.grid(row=0, column=0, pady=10)
    window_type_clicked = tk.StringVar()
    window_type_clicked.set("Basic")
    window_type_dropdown = tk.OptionMenu(dropdown_frm, window_type_clicked, *window_type)
    window_type_dropdown.grid(row=0, column=0, padx=10)
    print()
    
