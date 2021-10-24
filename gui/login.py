import datetime  # we will use this for date objects
reg_status = 0

class Patient:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age


def getdetails(username, password):
    global reg_status

    f = open("User_data.txt", 'r')
    info = f.read()
    if username in info:
        reg_status = 0

        return reg_status #"Name Unavailable. Please Try Again"
    f.close()

    f = open("User_Data.txt", 'w')
    info = info + " " + username + " " + password
    f.write(info)
    reg_status =1

    return reg_status # succefully signed up


def checkdetails(username, password):

    f = open("User_Data.txt", 'r')
    info = f.read()
    info = info.split()
    if username in info:
        index = info.index(username) + 1
        usr_password = info[index]
        if usr_password == password:
            return 1
        #call zains parameters
        else:
            return 0 # wrong password


    else:
        return -1 # name not found sign up



person = Patient(
    "Parthav",
    "Patel",
    datetime.date(2001, 4, 11),  # year, month, day
    "McMaster University",
    "555 456 0987",
    "mahdih2@mcmaster.ca"
)