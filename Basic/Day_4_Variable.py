name = "Israk"
age = 22

print(name)
print(age)

name = "Ahmed"
age = 23

isAdult = True
isMarried = False
# print(isAdult)

print(name)
print(age)

# Exersise

personNameFirst = "Tonny"
personNameLast = "Stark"
personAge = 51
ispersonGenius = True

print("Name : "+personNameFirst+" "+personNameLast)
print("age " + str(personAge))  # int to str convert
print("Genius : " + str(ispersonGenius))

age = 12 

if age>18:
    print("You are an adult")
    print("You can vote")
    print("Your age : " + str(age))

elif age<18 and age>6:
    print("You are a Boy/Girl")
    print("Your age : " + str(age))

else:
    print("You are a Child")
    print("Your age : " + str(age))

print("End of this Program")
