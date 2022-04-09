import check
import find


def getNumber():
    value1 = int(input("Enter your 1st number:"))
    value2 = int(input("Enter your 2nd number:"))
    print("The number", check.checkNum(value1, value2), "is valid.")


getNumber()
