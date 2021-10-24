import tkinter as tk
from tkinter import ttk
from tkinter import *


window = tk.Tk()
window.title('Pacing Parameters')
window.geometry('1000x700')


window.tk.call("source", "forest-dark.tcl")
ttk.Style().theme_use('forest-dark')

tab = ttk.Notebook(window)
tab.grid(padx=30, pady=15)

my_frame1 = Frame(tab, width=500, height=500)
my_frame2 = Frame(tab, width=500, height=500)
my_frame3 = Frame(tab, width=500, height=500)
my_frame4 = Frame(tab, width=500, height=500)

tab.add(my_frame1, text="AOO")
tab.add(my_frame2, text="VOO")
tab.add(my_frame3, text="AAI")
tab.add(my_frame4, text="VVI")
###-------------AOO------------------------
ttk.Label(my_frame1, text="Lower Rate Limit (ppm) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=8, padx=10, pady=25)
LRL = ttk.Spinbox(my_frame1, from_=30, to=175, wrap=1)
LRL.grid(column=1, row=8, padx=10, pady=25)
LRL.insert(0,60)

ttk.Label(my_frame1, text="Upper Rate Limit (ppm) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=9, padx=10, pady=25)
URL = ttk.Spinbox(my_frame1, from_=50, to=175, wrap=1)
URL.grid(column=1, row=9, padx=10, pady=25)
URL.insert(0, 120)

ttk.Label(my_frame1, text="Atrial Amplitude (V) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=10, padx=10, pady=25)
AA = ttk.Spinbox(my_frame1, from_=0, to=5, wrap=1)
AA.grid(column=1, row=10, padx=10, pady=25)
AA.insert(0, 3.75)

ttk.Label(my_frame1, text="Atrial Pulse Width (ms) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=11, padx=10, pady=25)

APW = ttk.Spinbox(my_frame1, from_=0.05, to=1.9, increment=0.1, wrap=1)
APW.grid(column=1, row=11, padx=10, pady=25)
APW.insert(0, 0.4)


###-------------AAI------------------------
ttk.Label(my_frame3, text="Lower Rate Limit (ppm) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=8, padx=10, pady=25)
LRL = ttk.Spinbox(my_frame3, from_=30, to=175, wrap=1)
LRL.grid(column=1, row=8, padx=10, pady=25)
LRL.insert(0,60)

ttk.Label(my_frame3, text="Upper Rate Limit (ppm) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=9, padx=10, pady=25)
URL = ttk.Spinbox(my_frame3, from_=50, to=175, wrap=1)
URL.grid(column=1, row=9, padx=10, pady=25)
URL.insert(0, 120)

ttk.Label(my_frame3, text="Atrial Amplitude (V) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=10, padx=10, pady=25)
AA = ttk.Spinbox(my_frame3, from_=0, to=5, wrap=1)
AA.grid(column=1, row=10, padx=10, pady=25)
AA.insert(0, 3.75)

ttk.Label(my_frame3, text="Atrial Pulse Width (ms) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=11, padx=10, pady=25)

APW = ttk.Spinbox(my_frame3, from_=0.05, to=1.9, increment=0.1, wrap=1)
APW.grid(column=1, row=11, padx=10, pady=25)
APW.insert(0, 0.4)

ttk.Label(my_frame3, text="Atrial Refractory Period (ms) :",
          font=("DevaJu Serif", 10)).grid(column=2,
                                             row=8, padx=10, pady=25)
ARP = ttk.Spinbox(my_frame3, from_=150, to=500, increment=10, wrap=1)
ARP.grid(column=3, row=8, padx=10, pady=25)
ARP.insert(0, 250)

###-------------VOO------------------------
ttk.Label(my_frame2, text="Lower Rate Limit (ppm) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=8, padx=10, pady=25)
LRL = ttk.Spinbox(my_frame2, from_=30, to=175, wrap=1)
LRL.grid(column=1, row=8, padx=10, pady=25)
LRL.insert(0,60)

ttk.Label(my_frame2, text="Upper Rate Limit (ppm) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=9, padx=10, pady=25)
URL = ttk.Spinbox(my_frame2, from_=50, to=175, wrap=1)
URL.grid(column=1, row=9, padx=10, pady=25)
URL.insert(0, 120)

ttk.Label(my_frame2, text="Ventricular Amplitude (V) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=10, padx=10, pady=25)
VA = ttk.Spinbox(my_frame2, from_=0, to=5, wrap=1)
VA.grid(column=1, row=10, padx=10, pady=25)
VA.insert(0, 3.75)

VPW = ttk.Spinbox(my_frame2, from_=0.05, to=1.9, increment=0.1, wrap=1)
VPW.grid(column=1, row=11, padx=10, pady=25)
VPW.insert(0, 0.4)

ttk.Label(my_frame2, text="Ventricular Pulse Width (ms) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=11, padx=10, pady=25)

###-------------VII------------------------
ttk.Label(my_frame4, text="Lower Rate Limit (ppm) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=8, padx=10, pady=25)
LRL = ttk.Spinbox(my_frame4, from_=30, to=175, wrap=1)
LRL.grid(column=1, row=8, padx=10, pady=25)
LRL.insert(0, 60)

ttk.Label(my_frame4, text="Upper Rate Limit (ppm) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=9, padx=10, pady=25)
URL = ttk.Spinbox(my_frame4, from_=50, to=175, wrap=1)
URL.grid(column=1, row=9, padx=10, pady=25)
URL.insert(0, 120)

ttk.Label(my_frame4, text="Ventricular Amplitude (V) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=10, padx=10, pady=25)
VA = ttk.Spinbox(my_frame4, from_=0, to=5, wrap=1)
VA.grid(column=1, row=10, padx=10, pady=25)
VA.insert(0, 3.75)

VPW = ttk.Spinbox(my_frame4, from_=0.05, to=1.9, increment=0.1, wrap=1)
VPW.grid(column=1, row=11, padx=10, pady=25)
VPW.insert(0, 0.4)

ttk.Label(my_frame4, text="Ventricular Pulse Width (ms) :",
          font=("DevaJu Serif", 10)).grid(column=0,
                                             row=11, padx=10, pady=25)

ttk.Label(my_frame4, text="Ventricular Refractory Period (ms) :",
          font=("DevaJu Serif", 10)).grid(column=2,
                                             row=8, padx=10, pady=25)
VRP = ttk.Spinbox(my_frame4, from_=150, to=500,increment=10, wrap=1)
VRP.grid(column=3, row=8, padx=10, pady=25)
VRP.insert(0, 320)


window.mainloop()