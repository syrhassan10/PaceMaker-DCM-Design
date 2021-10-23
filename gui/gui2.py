import tkinter as tk
from tkinter import RAISED

from PIL import Image, ImageTk
import tkinter.font as tkFont

HEIGHT = 700
WIDTH = 800

root = tk.Tk()
root.title("Main Page")


canvas = tk.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()

frame = tk.Frame(root,bg='#80c1ff')
frame.place(relx =0, rely =0, relwidth =0.4, relheight = 1)

frame2 = tk.Frame(root,bg='white')
frame2.place(relx =0.4, rely =0, relwidth =0.6, relheight = 1)


entry1 =tk.Entry(frame2, bd = 3)
entry1.place(relx=0.3, rely =0.5, relwidth =0.4, relheight =0.04)

entry2 =tk.Entry(frame2, show="*", bd = 3)
entry2.place(relx=0.3, rely =0.55, relwidth =0.4, relheight =0.04)


b_login = tk.Button(frame2, text="Sign In")
b_login.place(relx=0.3, rely =0.6, relwidth =0.3, relheight =0.05)

b_reg = tk.Button(frame2, text="New Account")
b_reg.place(relx=0.35, rely =0.7, relwidth =0.3, relheight =0.05)

#mcmaster
logo = Image.open('maclogo2.png')

w_size = 0.6*WIDTH
h_size = 0.37*HEIGHT
logo = logo.resize((int(w_size),int(h_size)))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(frame2, image=logo,  bg='white')
logo_label.image = logo
logo_label.place(relx=0.1, rely =0.1, relwidth =0.8, relheight =0.3)

#heart
heart_logo = Image.open('heart.png')

w2_size = 0.3*WIDTH
h2_size = 0.34*HEIGHT
heart_logo = heart_logo.resize((int(w2_size),int(h2_size)))
heart_logo = ImageTk.PhotoImage(heart_logo)

logo_label = tk.Label(frame, image=heart_logo, bg='#80c1ff')
logo_label.image = heart_logo
logo_label.place(relx=0.15, rely =0.1, relwidth =0.7, relheight =0.4)

#
var = tk.StringVar()
title_label = tk.Label(frame, textvariable=var, bg='#80c1ff')

var.set("Pacemaker DCM v1 - 2021-10-22")

title_label.place(relx=0.1, rely =0.7, relwidth =0.7, relheight =0.4)

root.mainloop()