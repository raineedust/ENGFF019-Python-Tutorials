# Career Test
#
# This program is provided as a Python pair-programming assessment.
#
# Co-Authored by:
# Names: Anthony Saopa Phiri | Tan Jin Yi
# Student IDs: 20401485 | 20396553


from careerQuestions import careerInput


def nameLol():
    print("Hello, welcome to our Career Test!")
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    name = firstName + " " + lastName
    startLol(name)


def startLol(name):
    print("Hi ", name)
    startTest = int(
        input("Please enter (1) to start the test, or (0) to end your session.")
    )
    hoorayLol(startTest, name)


def hoorayLol(startTest, name):
    if startTest in (1, 0):
        while True:
            if startTest == 1:
                careerInput(startTest)
                check = input(
                    "Hooray! You have come to the end of your session. Click any button to proceed..."
                )
                startLol(name)


nameLol()

# Note to Dr. Reginary:
#
# We did not implement error checking for the name, as some people may prefer to be anonymous and use nicknames / usernames instead.
#
# the if statement for startTest essentially functions as error checking.

# differentiate for careerResult disagree T YES

# restart program A

# error check in non-separate module A

# more than one user define func AT

# for loop logic T
