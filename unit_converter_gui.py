"""
Unit Converter GUI
- conversion will occur with pressing right arrow button
- dropdown menus for the converted unit and the converting unit 
- dropdown for the type of unit (distance, volume, mass, temperature)
- dropdown allowing switching between basic, scientific, and unit converter
- label for unit converted to; entry box for unit to convert

"""

import tkinter as tk
import unit_converter
#import main
from window import *

#from window import *
frames = []
dropdowns = []


def chnge_measurements():
    global main_option
    if measurement_clicked.get() == "mass":
        main_option = mass_options
        convert_unit_clicked.set("ounces")
        converted_unit_clicked.set("ounces")
    elif measurement_clicked.get() == "volume":
        main_option = volume_options
        convert_unit_clicked.set("ounces")
        converted_unit_clicked.set("ounces")
    elif measurement_clicked.get() == "temperature":
        main_option = temp_options
        convert_unit_clicked.set("\N{DEGREE FAHRENHEIT}")
        converted_unit_clicked.set("\N{DEGREE FAHRENHEIT}")
    elif measurement_clicked.get() == "distance":
        main_option = distance_options
        convert_unit_clicked.set("inches")
        converted_unit_clicked.set("inches")

    convert_unit_dropdown = tk.OptionMenu(convert_frm, convert_unit_clicked, *main_option) # Dynamically switch between options depending on measurement type
    convert_unit_dropdown.grid(row=0, column=1, sticky="w")
    converted_unit_dropdown = tk.OptionMenu(converted_frame, converted_unit_clicked, *main_option) # Dynamically switch between options depending on measurement type
    converted_unit_dropdown.grid(row=0, column=1, sticky="w")

def dropdown():
    convert_unit_clicked = tk.StringVar()
    if main_option == mass_options or main_option == volume_options:
        convert_unit_clicked.set("ounces")
    elif main_option == distance_options:
        convert_unit_clicked.set("inches")
    elif main_option == temp_options:
        convert_unit_clicked.set("\N{DEGREE FAHRENHEIT}")
    convert_unit_dropdown = tk.OptionMenu(convert_frm, convert_unit_clicked, *main_option) # Dynamically switch between options depending on measurement type
    convert_unit_dropdown.grid(row=0, column=1, sticky="w")

def convert():
    if main_option == mass_options:
        final = unit_converter.mass(main_option.index(convert_unit_clicked.get()), main_option.index(converted_unit_clicked.get()), float(convert_entry.get()))
    elif main_option == volume_options:
        final = unit_converter.volume(main_option.index(convert_unit_clicked.get()), main_option.index(converted_unit_clicked.get()), float(convert_entry.get()))
    elif main_option == temp_options:
        final = unit_converter.temp(main_option.index(convert_unit_clicked.get()), main_option.index(converted_unit_clicked.get()), float(convert_entry.get()))
    elif main_option == distance_options:
        final = unit_converter.distance(main_option.index(convert_unit_clicked.get()), main_option.index(converted_unit_clicked.get()), float(convert_entry.get()))
    converted_lbl["text"] = str(final)

mass_options = unit_converter.mass_units
distance_options = unit_converter.distance_units
volume_options = unit_converter.volume_units
temp_options = unit_converter.temp_units
measurement_options = unit_converter.measurements
#window_types = main.window_type

main_option = mass_options

unit_conv_master_frm = tk.Frame(master=window)
#window = tk.Tk()
#window.title("CalcX - Unit Converter")

#clicked = tk.StringVar()
#measurement_dropdown = tk.OptionMenu(window, clicked, *measurement_options) 
#window.resizable(width=False, height=False)
dropdown_frm = tk.Frame(master=unit_conv_master_frm)
dropdown_frm.grid(row=0, column=0, pady=10)
#window_type_clicked = tk.StringVar()
#window_type_clicked.set("Unit Converter")
#window_type_dropdown = tk.OptionMenu(dropdown_frm, window_type_clicked, *window_types)
#window_type_dropdown.grid(row=0, column=0, padx=10)
measurement_clicked = tk.StringVar()
measurement_clicked.set("mass")
measurement_dropdown = tk.OptionMenu(dropdown_frm, measurement_clicked, *measurement_options)
measurement_dropdown.grid(row=0, column=1, padx=10)
change_button = tk.Button(master=dropdown_frm, text="Change Unit Type", command=chnge_measurements)
change_button.grid(row=0, column=2, padx=10)
unit_conv_frame = tk.Frame(master=unit_conv_master_frm)
unit_conv_frame.grid(row=1, column=0)

convert_frm = tk.Frame(master=unit_conv_frame, width=10)
btn_frm = tk.Frame(master=unit_conv_frame, width=10)
converted_frame = tk.Frame(master=unit_conv_frame, width=10)

convert_entry = tk.Entry(master=convert_frm, width=5)
convert_entry.grid(row=0, column=0, sticky="e")
#convert_label = tk.Label(master=convert_frm, text="in.")
#convert_label.grid(row=0, column=1, sticky="w")
convert_unit_clicked = tk.StringVar()
converted_unit_clicked = tk.StringVar()
chnge_measurements()
"""
if main_option == mass_options or main_option == volume_options:
    convert_unit_clicked.set("ounces")
elif main_option == distance_options:
    convert_unit_clicked.set("inches")
elif main_option == temp_options:
    convert_unit_clicked.set("\N{DEGREE FAHRENHEIT}")
    
convert_unit_dropdown = tk.OptionMenu(convert_frm, convert_unit_clicked, *main_option) # Dynamically switch between options depending on measurement type
convert_unit_dropdown.grid(row=0, column=1, sticky="w")
"""

right_btn = tk.Button(master=btn_frm, text="\N{RIGHTWARDS BLACK ARROW}", command=convert)
right_btn.grid(row=0, column=0)

converted_lbl = tk.Label(master=converted_frame, width=20, fg="black", bg="white")
converted_lbl.grid(row=0, column=0)
#converted_type = tk.Label(master=converted_frame, text="ft.")
#converted_type.grid(row=0, column=1)
"""
if main_option == mass_options or main_option == volume_options:
    converted_unit_clicked.set("ounces")
elif main_option == distance_options:
    converted_unit_clicked.set("feet")
elif main_option == temp_options:
    converted_unit_clicked.set("\N{DEGREE CELSIUS}")
converted_unit_dropdown = tk.OptionMenu(converted_frame, converted_unit_clicked, *main_option) # Dynamically switch between options depending on measurement type
converted_unit_dropdown.grid(row=0, column=1, sticky="w")
"""

convert_frm.grid(row=0, column=0, padx=5)
btn_frm.grid(row=0, column=1, padx=5)
converted_frame.grid(row=0, column=2, padx=5)

#window.mainloop()
