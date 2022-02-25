# # 1


# def main():
#     value = getNumber()
#     checkNum(value)


# def getNumber():
#     value = int(input("Enter your number:"))
#     return value


# def checkNum(value):
#     if value > 0:
#         print("It's a positive number!")
#     elif value == 0:
#         print("0 is a neutral number!")
#     else:
#         print("It's a negative number!")


# main()

# value = int(input("Enter your number:"))
# if value >= 0:
#     print("It's a positive number")

# else:
#     print("It's a negative number")

# # 2


# def getNumber():
#     value = int(input("Enter your number:"))
#     return check(value)


# def check(value):
#     if value >= 1 & value <= 1000 & value % 2 == 0:
#         print("Value is an even number.")
#     elif value >= 1 & value <= 1000 & value % 2 != 0:
#         print("Value is an odd number.")
#     else:
#         print("Value is out of range.")


# getNumber()

# # 3


# def readRecData():
#     print("Enter the length and width of the first rectangle below")
#     length1 = int(input("1st rectangle length:"))
#     width1 = int(input("1st rectangle width:"))
#     print("Enter the length and width of the second rectangle below")
#     length2 = int(input("2nd rectangle length:"))
#     width2 = int(input("2nd rectangle width:"))
#     return calculateArea(length1, width1, length2, width2)


# def calculateArea(length1, width1, length2, width2):
#     area1 = length1 * width1
#     area2 = length2 * width2
#     return compareArea(area1, area2)


# def compareArea(area1, area2):
#     if area1 == area2:
#         print("The areas are the same.")
#     else:
#         print("The areas are not the same.")


# readRecData()

# # 4


# def getData():
#     annualSalary = int(input("Please enter your annual salary in RM:"))
#     yearsEmployed = int(input("Please enter the number of years employed:"))
#     return checkQualification(annualSalary, yearsEmployed)


# def checkQualification(annualSalary, yearsEmployed):
#     if (annualSalary >= 5000) and (yearsEmployed >= 2):
#         print("You qualify for credit card application!")
#     else:
#         print("Sorry, you do not qualify for credit card application.")


# getData()

# # 5


# def getInput():
#     char = input("Enter a character here: ")
#     return checkChar(char)


# def checkChar(char):
#     if char.isalpha():
#         charMod = changeCase(char)
#         printCh(char, charMod)
#     else:
#         errMsg()


# def changeCase(char):
#     if char.isupper():
#         charMod = char.lower()
#         return charMod
#     elif char.islower():
#         charMod = char.upper()
#         return charMod


# def errMsg():
#     print("Invalid input. Please enter a single alphabet character.")


# def printCh(char, charMod):
#     print(char, "→", charMod)


# getInput()
