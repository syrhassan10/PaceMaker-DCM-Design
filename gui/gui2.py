import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime


from PIL import Image, ImageTk
import tkinter.font as tkFont

root = tk.Tk()
root.title("Main Page")
root.geometry('1000x700')

#s = serial.Serial("COM6", 115200) #baudrate thats controls the controller
#x = s.read()          # read one byte (another way to make a pacermaker unique)


# Import the tcl file
root.tk.call('source', 'forest-dark.tcl')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

messags_status = StringVar()
login_status = StringVar()

LRL_values = [30, 35, 40, 45, 50, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
              71,
              72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 100, 105, 110, 115, 120,
              125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175]
pulse_width_values = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8,
                      1.9]
amp_values = [0, 1.25, 2.5, 3.75, 5]

def programmable():
    window = tk.Tk()
    window.title('Pacing Parameters')
    window.geometry('1000x700')

    window.tk.call("source", "forest-dark.tcl")
    ttk.Style().theme_use('forest-dark')

    tab = ttk.Notebook(window)
    tab.grid(padx=30, pady=15)
    date_rt = tk.StringVar()
    date_rt.set(datetime.date.today())

    date = ttk.Label(window, textvariable=date_rt)
    date.place(relx=0.1, rely=0.8, relwidth=0.6, relheight=0.2)

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
    LRL = ttk.Spinbox(my_frame1, values=LRL_values, wrap=1)
    LRL.grid(column=1, row=8, padx=10, pady=25)
    LRL.insert(0, 60)

    ttk.Label(my_frame1, text="Upper Rate Limit (ppm) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=9, padx=10, pady=25)
    URL = ttk.Spinbox(my_frame1, from_=50, to=175, increment=5.0, wrap=1)
    URL.grid(column=1, row=9, padx=10, pady=25)
    URL.insert(0, 120)

    ttk.Label(my_frame1, text="Atrial Amplitude (V) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=10, padx=10, pady=25)
    AA = ttk.Spinbox(my_frame1,values=amp_values, wrap=1)
    AA.grid(column=1, row=10, padx=10, pady=25)
    AA.insert(0, 3.75)

    ttk.Label(my_frame1, text="Atrial Pulse Width (ms) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=11, padx=10, pady=25)

    APW = ttk.Spinbox(my_frame1, values=pulse_width_values, wrap=1)
    APW.grid(column=1, row=11, padx=10, pady=25)
    APW.insert(0, 0.4)

    ###-------------AAI------------------------
    ttk.Label(my_frame3, text="Lower Rate Limit (ppm) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=8, padx=10, pady=25)
    LRL = ttk.Spinbox(my_frame3, values=LRL_values, wrap=1)
    LRL.grid(column=1, row=8, padx=10, pady=25)
    LRL.insert(0, 60)

    ttk.Label(my_frame3, text="Upper Rate Limit (ppm) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=9, padx=10, pady=25)
    URL = ttk.Spinbox(my_frame3, from_=50, to=175, increment=5.0, wrap=1)
    URL.grid(column=1, row=9, padx=10, pady=25)
    URL.insert(0, 120)

    ttk.Label(my_frame3, text="Atrial Amplitude (V) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=10, padx=10, pady=25)
    AA = ttk.Spinbox(my_frame3, values=amp_values, wrap=1)
    AA.grid(column=1, row=10, padx=10, pady=25)
    AA.insert(0, 3.75)

    ttk.Label(my_frame3, text="Atrial Pulse Width (ms) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=11, padx=10, pady=25)

    APW = ttk.Spinbox(my_frame3, values=pulse_width_values, wrap=1)
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
    LRL = ttk.Spinbox(my_frame2, values=LRL_values, wrap=1)
    LRL.grid(column=1, row=8, padx=10, pady=25)
    LRL.insert(0, 60)

    ttk.Label(my_frame2, text="Upper Rate Limit (ppm) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=9, padx=10, pady=25)
    URL = ttk.Spinbox(my_frame2, from_=50, to=175, increment=5.0, wrap=1)
    URL.grid(column=1, row=9, padx=10, pady=25)
    URL.insert(0, 120)

    ttk.Label(my_frame2, text="Ventricular Amplitude (V) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=10, padx=10, pady=25)
    VA = ttk.Spinbox(my_frame2, values=amp_values, wrap=1)
    VA.grid(column=1, row=10, padx=10, pady=25)
    VA.insert(0, 3.75)

    ttk.Label(my_frame2, text="Ventricular Pulse Width (ms) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=11, padx=10, pady=25)
    VPW = ttk.Spinbox(my_frame2, values=pulse_width_values, wrap=1)
    VPW.grid(column=1, row=11, padx=10, pady=25)
    VPW.insert(0, 0.4)

    ###-------------VII------------------------
    ttk.Label(my_frame4, text="Lower Rate Limit (ppm) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=8, padx=10, pady=25)
    LRL = ttk.Spinbox(my_frame4, values=LRL_values, wrap=1)
    LRL.grid(column=1, row=8, padx=10, pady=25)
    LRL.insert(0, 60)

    ttk.Label(my_frame4, text="Upper Rate Limit (ppm) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=9, padx=10, pady=25)
    URL = ttk.Spinbox(my_frame4, from_=50, to=175, increment=5.0, wrap=1)
    URL.grid(column=1, row=9, padx=10, pady=25)
    URL.insert(0, 120)

    ttk.Label(my_frame4, text="Ventricular Amplitude (V) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=10, padx=10, pady=25)
    VA = ttk.Spinbox(my_frame4, values=amp_values, wrap=1)
    VA.grid(column=1, row=10, padx=10, pady=25)
    VA.insert(0, 3.75)

    VPW = ttk.Spinbox(my_frame4, values=pulse_width_values, wrap=1)
    VPW.grid(column=1, row=11, padx=10, pady=25)
    VPW.insert(0, 0.4)

    ttk.Label(my_frame4, text="Ventricular Pulse Width (ms) :",
              font=("DevaJu Serif", 10)).grid(column=0,
                                              row=11, padx=10, pady=25)

    ttk.Label(my_frame4, text="Ventricular Refractory Period (ms) :",
              font=("DevaJu Serif", 10)).grid(column=2,
                                              row=8, padx=10, pady=25)
    VRP = ttk.Spinbox(my_frame4, from_=150, to=500, increment=10, wrap=1)
    VRP.grid(column=3, row=8, padx=10, pady=25)
    VRP.insert(0, 320)

    window.mainloop()


def set_communication(button):
    # serial comm to connect to the board
    button.configure(text="CONNECTED")


def getdetails(username, password, retypedpassword):
    global messags_status
    global num_users
    f = open("User_data.txt", 'r')
    ting = f.readlines()

    num_users = len(ting)

    for line in ting:
        temp = line.split(" ")
        if username == temp[0]:
            messags_status.set("Name Unavailable. Please Try Again")
            f.close()
            return 0

    if num_users == 10:
        reg_status = 0
        messags_status.set("Cannot exceed limit of 10 registered users")
        return reg_status
    f.close()
    if password != retypedpassword:
        messags_status.set("Passwords do not match")
        return 0

    with open('User_data.txt', 'a') as a_writer:
        acc_details = "\n" + username + ' ' + password
        a_writer.write(acc_details)
    messags_status.set("successfully signed up")
    num_users += 1
    a_writer.close()
    root.destroy()
    programmable()


def checkdetails(username, password):
    global login_status

    f = open("User_Data.txt", 'r')
    info = f.read()
    info = info.split()
    if username in info:
        index = info.index(username) + 1
        usr_password = info[index]
        if usr_password == password:
            login_status.set("successfully signed in")
            root.destroy()
            programmable()

        # call zains parameters
        else:
            login_status.set("Wrong password")



    else:
        login_status.set("username not found")


def register_new_user():
    global messags_status
    labelText = tk.StringVar()
    labelText.set("Username: ")
    labelDir = ttk.Label(root, textvariable=labelText)
    labelDir.place(relx=0.6, rely=0.55, relwidth=0.1, relheight=0.04)

    dirname = ttk.Entry(root)
    dirname.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.04)

    labelText2 = tk.StringVar()
    labelText2.set("Password: ")
    labelDir2 = ttk.Label(root, textvariable=labelText2)
    labelDir2.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.04)

    dirpass = ttk.Entry(root)
    dirpass.place(relx=0.6, rely=0.7, relwidth=0.2, relheight=0.04)

    labelText3 = tk.StringVar()
    labelText3.set("Retype Password: ")
    labelDir3 = ttk.Label(root, textvariable=labelText3)
    labelDir3.place(relx=0.6, rely=0.75, relwidth=0.15, relheight=0.04)

    dirname3 = ttk.Entry(root)
    dirname3.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.04)

    b_register = ttk.Button(root, text="Register",
                            command=lambda: getdetails(dirname.get(), dirpass.get(), dirname3.get()))  # writes to file
    b_register.place(relx=0.65, rely=0.85, relwidth=0.1, relheight=0.07)

    messaage = ttk.Label(root, textvariable=messags_status)
    # messags_status.set("Click Register")
    messaage.place(relx=0.65, rely=0.93, relwidth=0.3, relheight=0.05)

    root.mainloop()


def intial_screen():
    global login_status

    frame2 = tk.Frame(root)
    frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelDir = ttk.Label(frame2, text="Username:")
    labelDir.place(relx=0.08, rely=0.47, relwidth=0.1, relheight=0.1)

    labelDir2 = ttk.Label(frame2, text="Password:")
    labelDir2.place(relx=0.08, rely=0.53, relwidth=0.1, relheight=0.08)

    # Username
    entry1 = ttk.Entry(frame2)
    entry1.place(relx=0.15, rely=0.5, relwidth=0.2, relheight=0.04)
    # Password
    entry2 = ttk.Entry(frame2, show="*")
    entry2.place(relx=0.15, rely=0.55, relwidth=0.2, relheight=0.04)

    b_login = ttk.Button(frame2, text="Sign In", command=lambda: checkdetails(entry1.get(), entry2.get()))
    b_login.place(relx=0.15, rely=0.6, relwidth=0.1, relheight=0.05)

    messaage1 = ttk.Label(root, textvariable=login_status)
    login_status.set("Login")
    messaage1.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.05)

    ##--------------------- register -------------------

    b_new_acc = ttk.Button(frame2, text="New Account", command=lambda: register_new_user())
    b_new_acc.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.05)

    # heart
    heart_logo = Image.open('heart.png')

    w2_size = 0.3 * 1000
    h2_size = 0.4 * 700
    heart_logo = heart_logo.resize((int(w2_size), int(h2_size)))
    heart_logo = ImageTk.PhotoImage(heart_logo)

    logo_label = ttk.Label(frame2, image=heart_logo)
    logo_label.image = heart_logo
    logo_label.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.4)

    #

    title_label = ttk.Label(frame2, text="Pacemaker DCM v1 - 2021-10-22")
    title_label.place(relx=0.1, rely=0.8, relwidth=0.5, relheight=0.1)

    b_comm = ttk.Button(frame2, text="CONNECT", command=lambda: set_communication(b_comm))
    b_comm.place(relx=0.1, rely=0.9, relwidth=0.3, relheight=0.05)

    root.mainloop()


intial_screen()