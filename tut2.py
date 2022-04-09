# Tutorial 2

# 1

print(format(12356.29, ".1f"))
print(format(12356.899, ".2f"))
print(format(12356.899, ".3f"))
print(format(12356.8990, ".3f"))
print(format(12356.8999, ".3f"))
print(round(12356.879))
print(round(12359.809))

# Answer:
#
# 12356.3
# 12356.90
# 12356.899
# 12356.899
# 12356.900
# 12357
# 12360

# 2

# Answer:
#
# int, float, str

# 3

print("Hello" + "how are" + "you?")

# Answer:
#
# Hellohow areyou?

# 4

myValue = 99
myValue = 10
myValue = myValue + 15
print(myValue)

# Answer:
#
# 25

# 5

Number1 = 100
Number2 = 25
Product = Number1 * number2

# Answer:
#
# NameError

# 6

value1 = 2.6
value2 = int(value1)
value3 = -2.9
value4 = int(value3)
value5 = 2
value6 = float(value5)
print("\n", value2, "\n", value4, "\n", value6)

# Answer:
#
# 2
# -2
# 2.0

# 7

amountDue = 5000.0
monthlyPayment = amountDue / 12
print("The monthly payment is", format(monthlyPayment, ".2f"))

# Answer:
#
# The monthly payment is 416.67

# 8

score = 99
name = input("Enter your name :")
print(name, "your score is", score)

# Answer:
#
# 1 3 2

# 9

PI = 3.14159  # constant variable
r = float(input("Enter radius"))
area = PI * r ** 2
print("Area is", area)

# 10

ProductCode = "ABC1190"
ProductName = "Sony DVD Player"
ProductPrice = str(350.00)
print(ProductCode + " " + ProductName + " RM " + ProductPrice)

# 11

firstName = "John"
lastName = "Kevin"
print(firstName, lastName)

# 12

A = 5
B = 10
C = B % A
print(C % 0)

# Answer:
#
# In Mathematics, when a number is divided by a zero, the result is an infinite number.

# 13

firstName = input("Enter your first name:")
lastName = input("Enter your last name:")
print("Hello", firstName, ",", lastName)

# 14

name = input("Enter your name:")
yearOfBirth = int(input("Enter your year of birth YYYY:"))
yearOld = 2022 - yearOfBirth
print("Hi", name, "you're", yearOld, "years old")

# 15

import math

# Gather data

radius = float(input("Enter the cone radius:"))
height = float(input("Enter the cone height:"))

# Input formula and display result

volume = math.pi * radius ** 2 * height / 3
print("The cone volume is:", volume)
