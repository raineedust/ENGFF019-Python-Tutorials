# 1

integerList = list(range(101))
print(integerList)

# 2

bookList = []


def main():
    while True:
        bookTitle = input("Enter the book title:\n")
        addAnother = input("\nDo you want to add another item? ")
        bookList.append(bookTitle)
        if addAnother.upper() == "Y":
            continue
        else:
            print("\nProgram terminated successfully. Here is the final book list:\n")
            print("-" * 30)
            print("Book Titles")
            print("-" * 30)
            for (i, bookOutput) in enumerate(bookList, start=1):
                print(bookOutput.capitalize())
            print("-" * 30)
            print("Total number of books is:", len(bookList))
            break


main()

# 3

romanList = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
wordList = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    number = int(input("Enter a number:"))
    if number >= 0 & number <= 10:
        findIndex = numberList.index(number)
        print("The Roman numeral for", wordList[findIndex], "is", romanList[findIndex])
    else:
        print("Invalid data entered, please try again.")
    addAnother = input("Do you want to enter another number?")
    if addAnother.upper() == "Y":
        continue
    else:
        print("Program terminated successfully. Thanks for using our service!")
        break

# 4

record1 = ("John Smith", "Savings", "12345678900")

record1List = list(record1)
record1List[2] = "123445678"

record1 = tuple(record1List)
print(record1)

# 5

thisTuple = (
    0,
    1,
    1,
    0,
    -1,
    -1,
    0,
    1,
    1,
    0,
    1,
    0,
    -1,
    -1,
    0,
    0,
    -1,
    1,
    1,
    0,
    0,
    1,
    -1,
    -1,
)

countZero = 0
countOne = 0
countNeg = 0

# insert a for loop here

for i in thisTuple:
    if i == 0:
        countZero += 1

for i in thisTuple:
    if i == 1:
        countOne += 1

for i in thisTuple:
    if i == -1:
        countNeg += 1

print("-" * 30)
print("No of zeros            :", countZero)
print("No of ones             :", countOne)
print("No of negative numbers :", countNeg)
print("-" * 30)


# 6

# replace all zeros to -1 and ones to -2


thisTuple = (0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1)
temp = list(thisTuple)

# insert a for loop here

for i in range(len(temp)):
    if temp[i] == 0:
        temp[i] = -1
    if temp[i] == 1:
        temp[i] = -2

thisTuple = tuple(temp)
print(thisTuple)
