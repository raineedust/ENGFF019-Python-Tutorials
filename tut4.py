# 1

value = int(input("Enter your number:"))

if value >= 1 and value <= 1000:
    if value % 2 == 0:
        print("even number")

    elif value % 2 != 0:
        print("odd number")

else:
    print("Invalid input, please try again!")

# 2 AreaRectangle.py

print("Enter the length and width of the first rectangle below")
length1 = float(input("1st rectangle length:"))
width1 = float(input("1st rectangle width:"))

print("Enter the length and width of the second rectangle below")
length2 = float(input("2nd rectangle length:"))
width2 = float(input("2nd rectangle width:"))

area1 = format(length1 * width1, ".2f")
area2 = format(length2 * width2, ".2f")

strArea1 = str(area1)
strArea2 = str(area2)

if area1 == area2:
    print("The areas are the same.")

elif area1 > area2:
    print(strArea1 + " of first rectangle is greater than the second rectangle.")

elif area2 > area1:
    print(strArea2 + " of second rectangle is greater than the first rectangle.")

else:
    print("The areas are not the same.")

# 3 CreditCard.py

annualSalary = int(input("Please enter your annual salary in RM:"))
yearsEmployed = int(input("Please enter the number of years employed:"))

if (annualSalary >= 5000) and (yearsEmployed >= 2):
    print("You qualify for credit card application!")

elif (annualSalary < 5000) and (yearsEmployed >= 2):
    print(
        "Sorry, you do not qualify for credit card application. Your salary, RM "
        + str(annualSalary)
        + ", is less than the minimum RM 5000."
    )

elif (annualSalary >= 5000) and (yearsEmployed < 2):
    print(
        "Sorry, you do not qualify for credit card application. Your years employed, "
        + str(yearsEmployed)
        + " year(s), is less than the minimum 2 years."
    )

else:
    print(
        "Sorry, you do not qualify for both criteria of our credit card application. \nYour salary, RM "
        + str(annualSalary)
        + ", is less than the minimum RM 5000. \nYour years employed, "
        + str(yearsEmployed)
        + " year(s), is less than the minimum 2 years."
    )

# 4

# database

intToRoman = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
}

# input

int = int(input("Enter a number: "))

# output

if int == 1:
    print("The Roman numeral is: I")

elif int == 3:
    print("The Roman numeral is: III")

elif int == 4:
    print("The Roman numeral is: IV")

elif int == 5:
    print("The Roman numeral is: V")

elif int == 6:
    print("The Roman numeral is: VI")

elif int == 7:
    print("The Roman numeral is: VII")

elif int == 8:
    print("The Roman numeral is: VIII")

elif int == 9:
    print("The Roman numeral is: IX")

elif int == 10:
    print("The Roman numeral is: X")

else:
    print("Data is invalid. Please restart the program.")

# 5

# input

weight = float(input("Please enter your weight in pounds:"))
height = float(input("Please enter your height in inches:"))

# calculate

bmi = weight * 703 / height ** 2

# user output

if bmi >= 25 and bmi <= 18.5:
    print("Your weight is optimal.")

elif bmi < 18.5:
    print("You are underweight.")

elif bmi > 25:
    print("You are overweight.")

else:
    print("Data is invalid. Please restart the program.")
