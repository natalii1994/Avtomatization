class User:

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def outputFirstName(self):
        print("Меня зовут", self.fname)

    def outputLastName(self):
        print("Моя фамилия", self.lname)
    
    def outputFirstNameAndLastName(self):
       print("Меня зовут", self.fname, self.lname) 