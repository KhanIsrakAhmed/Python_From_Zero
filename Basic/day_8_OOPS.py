# -------------------------------------------------------------------- Create Class In Python

class Student:
    def __init__(self, fname, lname, cgpa, age):   # Constructor
        self.first_name = fname
        self.last_name = lname
        self.cgpa = cgpa
        self.age = age

    def printFullName(self):            # create Function into a Class
        print(self.first_name + ' ' + self.last_name)
