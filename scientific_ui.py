"""
CalcX by tyiop794

A calculator and unit converter combo; primarily functions as a calculator
- Make it easy to switch between calculator and unit converter (also add scientific function for more abilities)
- Buttons are easy to access; is of a decent size
- should not be resizable
- when signs are clicked, they should change color to show they are active
- use dictionary or 2d array to link operation symbol with operation function in calculate.py
"""

import tkinter as tk
import calculate
#import main
from window import *

num_loc = []

oper_used = []
nums_operate = []

def oper_color(operation):
    # Changes color of sign if the operation is currently in use
    # Once operation no longer in use, change sign back to using black foreground
    for i in range(0, 5):
        # fg="green" if button is active
        if operations[i] == operation and operation != "=":
            oper_btns[i] = tk.Button(master=basic_btn_frame, text=operations[i], command=lambda i = i: sign_init(operations[i]), fg="green")
        else:
            oper_btns[i] = tk.Button(master=basic_btn_frame, text=operations[i], command=lambda i = i: sign_init(operations[i]), fg="black")
        oper_btns[i].grid(row=i, column=3, padx=5, pady=5, sticky="ew")

def switch_calcs():
    print("This is a test function for the time being")


def nums(num):
    if lbl["text"] == "0" or lbl["text"] in nums_operate:
        lbl["text"] = (num)
    else:
        lbl["text"] += (num)

def ac():
    global oper_used
    global nums_operate
    lbl["text"] = "0"
    oper_used = []
    nums_operate = []
    oper_color("=")
    

def change_sign():
    scnd_num = lbl["text"]
    if scnd_num[0] == "-":
        scnd_num = scnd_num[1:]
    else:
        scnd_num = "-" + scnd_num
    lbl["text"] = scnd_num

def percent():
    value = float(lbl["text"])
    value *= 0.01
    lbl["text"] = str(value)

def sign_init(operation):
    global nums_operate
    global oper_used
    new_num = 0
    if len(nums_operate) == 1:
        if oper_used[0] == "=":
            oper_used.append(operation)
            oper_used.pop(0)
        elif oper_used[0] not in operations:
            oper_used.append(operation)
            adv_init(oper_used[0])
        else:
            nums_operate.append(lbl["text"])
            if oper_used[0] == "/":
                new_num = calculate.divide_decimal(float(nums_operate[0]), float(nums_operate[1]))
            elif oper_used[0] == "X":
                new_num = calculate.multiply(float(nums_operate[0]), float(nums_operate[1]))
            elif oper_used[0] == "+":
                new_num = calculate.add(float(nums_operate[0]), float(nums_operate[1]))
            elif oper_used[0] == "-":
                new_num = calculate.subtract(float(nums_operate[0]), float(nums_operate[1]))
            oper_used[0] = operation
            nums_operate = []
            nums_operate.append(new_num)
            lbl["text"] = new_num
    else:
        nums_operate.append(lbl["text"])
        oper_used.append(operation)
    oper_color(oper_used[0])

def adv_init(operation):
    global nums_operate
    global oper_used
    print("This is a test function")
    if len(oper_used) > 0:
        nums_operate.append(lbl["text"])
        if oper_used[0] == oper_adv[0]:
            new_num = calculate.ee(float(nums_operate[0]), float(nums_operate[1]))
        elif oper_used[0] == oper_adv[2]:
            new_num = calculate.num_root(float(nums_operate[0]), float(nums_operate[1]))
        elif oper_used[0] == oper_adv[3]:
            new_num = calculate.num_exp(float(nums_operate[0]), float(nums_operate[1]))
        nums_operate = []
        oper_used = []
        lbl["text"] = new_num
        oper_used.pop(0)
    elif oper_adv.index(operation) in adv_one:
        nums_operate = []
        nums_operate.append(lbl["text"])
        if operation == oper_adv[1]:
            new_num = calculate.pi()
        elif operation == oper_adv[4]:
            new_num = calculate.sin(float(nums_operate[0]))
        elif operation == oper_adv[5]:
            new_num = calculate.ln(float(nums_operate[0]))
        elif operation == oper_adv[6]:
            new_num = calculate.log_ten(float(nums_operate[0]))
        elif operation == oper_adv[7]:
            new_num = calculate.sqroot(float(nums_operate[0]))
        elif operation == oper_adv[8]:
            new_num = calculate.num_sqrd(float(nums_operate[0]))
        elif operation == oper_adv[9]:
            new_num = calculate.cos(float(nums_operate[0]))
        lbl["text"] = new_num
        nums_operate.pop(0)
    elif oper_adv.index(operation) in adv_two:
        nums_operate.append(lbl["text"])
        oper_used.append(operation)
        #oper_color(oper_used[0])


operations = ["A/C", "+/-", "%", "/"]
scientific_frm = tk.Frame(master=window)
#window = tk.Tk()
#window.resizable(width=False, height=False)
#window.title("CalcX")
lbl_frame=tk.Frame(master=scientific_frm)
lbl_frame.pack()
lbl = tk.Label(master=lbl_frame, bg="white", fg="black", width=50, text="0", anchor="e", justify=tk.LEFT)
lbl.pack(side=tk.RIGHT)

dropdown_frame = tk.Frame(master=scientific_frm)
dropdown_frame.pack()
dropdown_test = tk.Button(master=dropdown_frame, text="Test", width=25)
dropdown_test.pack(side=tk.LEFT)

btn_frame = tk.Frame(master=scientific_frm) 
btn_frame.pack(side=tk.RIGHT)

adv_btn_frame = tk.Frame(master=btn_frame)
adv_btn_frame.grid(row=0, column=0, sticky="e")

basic_btn_frame = tk.Frame(master=btn_frame)
basic_btn_frame.grid(row=0, column=1, sticky="e")

clear_btn = tk.Button(master=basic_btn_frame, text="A/C", command=ac, fg="red")
clear_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

sign_btn = tk.Button(master=basic_btn_frame, text="+/-", command=change_sign)
sign_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

percent_btn = tk.Button(master=basic_btn_frame, text="%", command=percent)
percent_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

operations = ["/", "X", "-", "+", "="]
oper_btns = []
for i in range(0, 5):
    # fg="green" if button is active
    oper_btns.append(tk.Button(master=basic_btn_frame, text=operations[i], command=lambda i = i: sign_init(operations[i]), fg="black"))
    oper_btns[i].grid(row=i, column=3, padx=5, pady=5, sticky="ew")

oper_adv = ["EE", "π", "(y)√x", "x^y", "sin", "ln", "log10", "√x", "x^2", "cos"]
adv_btns_one = []
adv_btns_two = []
adv_one = [1, 4, 5, 6, 7, 8, 9]
adv_two = [0, 2, 3]
z = 0
a = 5
"""
for x in range(0, 2):
    for i in range(z, a):
        adv_btns.append(tk.Button(master=adv_btn_frame, text=oper_adv[i], command=lambda i = i: adv_init(oper_adv[i]), fg="black"))
        adv_btns[i].grid(row=i, column=x, padx=5, pady=5, sticky="ew")
"""
y = 0
for x in range(0, 2):
    if x == 1:
        z += 5
        a += 5
    for i in range(z, a):
        if i in adv_one:
            adv_btns_one.append(tk.Button(master=adv_btn_frame, text=oper_adv[i], command=lambda i = i: adv_init(oper_adv[i]), fg="black"))
            adv_btns_one[len(adv_btns_one) - 1].grid(row=y, column=x, padx=5, pady=5, sticky="ew")
        elif i in adv_two:
            adv_btns_two.append(tk.Button(master=adv_btn_frame, text=oper_adv[i], command=lambda i = i: adv_init(oper_adv[i]), fg="black"))
            adv_btns_two[len(adv_btns_two) - 1].grid(row=y, column=x, padx=5, pady=5, sticky="ew")
        y += 1
    y = 0

    


num = 0
num_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
num_btns = []
for i in range(3, 0, -1):
    if i == 3:
        num = 1
    elif i == 2:
        num = 4
    elif i == 1:
        num = 7
    for x in range(0, 3):
        calc_num = x + num
        num_btns.append(tk.Button(master=basic_btn_frame, text=str(calc_num), command=lambda calc_num = calc_num : nums(str(calc_num))))
        num_btns[calc_num - 1].grid(row=i, column=x, padx=5, pady=5, sticky="ew")


zero_btn = tk.Button(master=basic_btn_frame, text="0", command=lambda: nums(str(0)))
zero_btn.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

deci_btn = tk.Button(master=basic_btn_frame, text=".", command=lambda: nums("."))
deci_btn.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

#window.mainloop()