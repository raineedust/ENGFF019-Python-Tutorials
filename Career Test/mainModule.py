# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553


import careerQuestions
import errorCheck


def main():
    print(
        "Hello, welcome to the Career Test!/n",
    )
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    name = firstName, lastName

    # Capturing the users' name, and checking for any error.

    print("Welcome ", name, sep="")
    startTest = int(
        input("Click (1) to start the test, and click (2) to end your session")
    )
    career = "lol"

    # Prompting the user to begin the test.

    print(name, ", an ideal career choice for you would be ", career)


main()
