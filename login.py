import datetime # we will use this for date objects

class Patient:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone  = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Patient(
    "Parthav",
    "Patel",
    datetime.date(2001, 4, 11), # year, month, day
    "McMaster University",
    "555 456 0987",
    "mahdih2@mcmaster.ca"
)

print(person.name)
print(person.email)
print(person.age())
print(datetime.date.today())