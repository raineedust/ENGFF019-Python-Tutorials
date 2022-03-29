# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553


from careerQuestions import careerInput
import errorCheck
import careerResult


def main():
    print(
        "Hello, welcome to the Career Test",
    )
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    name = firstName, lastName

    # Capturing the users' name, and checking for any error.

    print("Welcome ", name)
    startTest = int(
        input("Enter (1) to start the test, and enter (2) to end your session")
    )
    careerInput(startTest)

    # Prompting the user to begin the test.


main()
