# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553


from careerQuestions import careerInput
import careerResult

startTest = 1

while startTest == True:

    def main():
        print("Hello, welcome to our Career Test!")
        firstName = input("Please enter your first name: ")
        lastName = input("Please enter your last name: ")
        if firstName.isalpha() and lastName.isalpha():
            name = firstName + " " + lastName
        else:
            print("Error! Your name should only contain letters.")
        return

    def test():
        startTest = int(
            input("Please enter (1) to start the test, or (0) to end your session.")
        )
        careerInput(startTest)

    continue


main()


# differentiate for careerResult disagree T YES

# restart program A

# error check in non-separate module A

# more than one user define func AT

# for loop logic T
