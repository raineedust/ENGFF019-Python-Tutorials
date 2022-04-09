# 1 PosNegNumbers.py

value = int(input("Enter your number:"))
if value >= 0:
    print("It's a positive number")

else:
    print("It's a negative number")

# 2 EvenOdd.py

value = int(input("Enter your number:"))

if value % 2 == 0:
    print("even number")

else:
    print("odd number")

# 3 AreaRectangle.py

print("Enter the length and width of the first rectangle below")
length1 = int(input("1st rectangle length:"))
width1 = int(input("1st rectangle width:"))

print("Enter the length and width of the second rectangle below")
length2 = int(input("2nd rectangle length:"))
width2 = int(input("2nd rectangle width:"))

area1 = length1 * width1
area2 = length2 * width2

if area1 == area2:
    print("The areas are the same.")
else:
    print("The areas are not the same.")

# 4 CreditCard.py

annualSalary = int(input("Please enter your annual salary in RM:"))
yearsEmployed = int(input("Please enter the number of years employed:"))

if (annualSalary >= 5000) and (yearsEmployed >= 2):
    print("You qualify for credit card application!")
else:
    print("Sorry, you do not qualify for credit card application.")

# 5 MagicDates.py

print("Enter the date in the following format:[dd/mm/yy]")
day = int(input("What is the day? :"))
month = int(input("What is the month? :"))
year = int(input("What is the year? :"))

if month * day == year:
    print(day, "/", month, "/", year, "is a magic date!")
else:
    print("Unfortunately", ",", day, "/", month, "/", year, "is not a magic date.")
