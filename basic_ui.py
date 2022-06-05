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

num_loc = []

oper_used = []
nums_operate = []

def oper_color(operation):
    # Changes color of sign if the operation is currently in use
    # Once operation no longer in use, change sign back to using black foreground
    for i in range(0, 5):
        # fg="green" if button is active
        if operations[i] == operation and operation != "=":
            oper_btns[i] = tk.Button(master=btn_frame, text=operations[i], command=lambda i = i: sign_init(operations[i]), fg="green")
        else:
            oper_btns[i] = tk.Button(master=btn_frame, text=operations[i], command=lambda i = i: sign_init(operations[i]), fg="black")
        oper_btns[i].grid(row=i, column=3, padx=5, pady=5, sticky="ew")


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


operations = ["A/C", "+/-", "%", "/"]
window = tk.Tk()
window.resizable(width=False, height=False)
window.title("CalcX")
lbl_frame=tk.Frame(master=window)
lbl_frame.pack()
lbl = tk.Label(master=lbl_frame, bg="white", fg="black", width=25, text="0", anchor="e", justify=tk.LEFT)
lbl.pack(side=tk.RIGHT)
lbl.grid(row=0, column=0, sticky="e")

btn_frame = tk.Frame(master=window)
btn_frame.pack()

clear_btn = tk.Button(master=btn_frame, text="A/C", command=ac, fg="red")
clear_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

sign_btn = tk.Button(master=btn_frame, text="+/-", command=change_sign)
sign_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

percent_btn = tk.Button(master=btn_frame, text="%", command=percent)
percent_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

operations = ["/", "X", "-", "+", "="]
oper_btns = []
for i in range(0, 5):
    # fg="green" if button is active
    oper_btns.append(tk.Button(master=btn_frame, text=operations[i], command=lambda i = i: sign_init(operations[i]), fg="black"))
    oper_btns[i].grid(row=i, column=3, padx=5, pady=5, sticky="ew")


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
        num_btns.append(tk.Button(master=btn_frame, text=str(calc_num), command=lambda calc_num = calc_num : nums(str(calc_num))))
        num_btns[calc_num - 1].grid(row=i, column=x, padx=5, pady=5, sticky="ew")


zero_btn = tk.Button(master=btn_frame, text="0", command=lambda: nums(str(0)))
zero_btn.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

deci_btn = tk.Button(master=btn_frame, text=".", command=lambda: nums("."))
deci_btn.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

window.mainloop()