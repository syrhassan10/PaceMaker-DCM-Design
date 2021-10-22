import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont


def main_screen():
    global root
    root = tk.Tk()
    root.title("Pacemaker - 3K04")
    canvas = tk.Canvas(root, width=1000, height=600)
    canvas.grid(columnspan=3, rowspan=4)

    logo = Image.open('maclogo2.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo

    logo_label.grid(column=1, row=0)

    # main body
    instructions = tk.Label(root, text="Please choose one of the options to continue", font="Raleway")
    instructions.grid(columnspan=3, column=0, row=1)

    button_login = tk.Button(text="Log in",
                             width=20,
                             height=3,
                             bg="grey",
                             fg="black",
                             command=login)

    button_login.grid(column=1, row=2)
    button_signup = tk.Button(text="Register",
                              width=20,
                              height=3,
                              bg="grey",
                              fg="black",
                              command=register)

    button_signup.grid(column=1, row=3)
    root.mainloop()


def register():
    global register_screen
    global username
    global password

    register_screen = tk.Tk()
    canvas = tk.Canvas(register_screen, width=600, height=400)
    canvas.grid(columnspan=2, rowspan=3)
    # root.destroy()
    register_screen.title("Register")

    font_style = tkFont.Font(family="Lucida Grande", size=25)

    label_username = tk.Label(register_screen, text="Username", font=font_style).grid(row=0, column=0)
    username = tk.StringVar()
    entry_username = tk.Entry(register_screen, textvariable=username).grid(row=0, column=1)

    label_password = tk.Label(register_screen, text="Password", font=font_style).grid(row=1, column=0)
    password = tk.StringVar()
    entry_password = tk.Entry(register_screen, textvariable=password, show='*').grid(row=1, column=1)

    button_register = tk.Button(register_screen, text="Register", width=10, height=1).grid(columnspan=2, row=2)

    create_user(str(username), str(password))  # call function to register the user


def create_user(username, password):
    if user_exists(username):
        print("username exists already")
        return False
    else:
        file = open("user_database.txt", "a")  # if the user does not exist, open file to append info
        file.write(username)  # Add username and password to new line
        file.write("\t")
        file.write(password)
        file.write("\n")
        file.close()
        return True


def get_user_data():
    file = open("user_database.txt", "r")  # Open file for reading
    usernames = []
    passwords = []
    for line in file:
        temp = line.strip("\n")  # Strip newline character
        temp2 = temp.split("\t")  # Split by tab character
        username = temp2[0]
        password = temp2[1]
        usernames.append(username)  # Add username and password to their respective lists
        passwords.append(password)
    file.close()  # Close the file
    return [usernames, passwords]


def user_exists(username):
    users = get_user_data()[0]
    if username in users:
        return True
    else:
        return False


def login():
    global login_screen
    font_style = tkFont.Font(family="Lucida Grande", size=25)

    login_screen = tk.Tk()
    login_screen.title("Login")

    canvas = tk.Canvas(login_screen, width=600, height=400)
    canvas.grid(columnspan=2, rowspan=4)

    tk.Label(login_screen, text="Please enter details below to login", font=font_style).grid(columnspan=2, row=0)

    global username_verify
    global password_verify

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    global username_login_entry
    global password_login_entry

    tk.Label(login_screen, text="Username ", font=font_style).grid(column=0, row=1)
    username_login_entry = tk.Entry(login_screen, textvariable=username_verify)
    username_login_entry.grid(column=1, row=1)

    tk.Label(login_screen, text="Password ", font=font_style).grid(column=0, row=2)
    password_login_entry = tk.Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.grid(column=1, row=2)

    tk.Button(login_screen, text="Login", width=10, height=1,
              command=user_login(username_verify, password_verify)).grid(columnspan=2, row=3)


def user_login(username, password):
    data = get_user_data()
    usernames, passwords = data[0], data[1]
    if user_exists(username):  # If the user exists, see if the password is correct
        i = usernames.index(username)  # Get the index in the userlist associated with username
        real_password = passwords[i]  # Use this index to find their password
        if password == real_password:  # Check if passwords match
            tk.Label(login_screen, text="Login Successful!", fg="green", bg="white").grid(columnspan=3, row=4)
            return True
        else:
            tk.Label(login_screen, text="Password is incorrect", fg="red", bg="white").grid(columnspan=3, row=4)
            return False
    else:  # If the user does not exist, return False
        return False


main_screen()

# https://www.simplifiedpython.net/python-gui-login/
