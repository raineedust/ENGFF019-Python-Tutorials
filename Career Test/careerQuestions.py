# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553


from careerResult import careerOutput


def careerInput(startTest):

    while startTest == 1:
        print("Please enter (1) if you agree, or (0) if you disagree.")

        creativeChoice = int(input("Would you enjoy designing a magazine cover? "))
        creativeChoice = (
            int(input("Would you enjoy taking pictures of nature? ")) + creativeChoice
        )

        stemChoice = int(input("Do scientific experiments interest you? "))
        stemChoice = (
            int(input("Does researching a new medicine sound attractive to you? "))
            + stemChoice
        )

        laborChoice = int(input("Would you enjoy installing a hardwood floor? "))
        laborChoice = (
            int(input("Do you enjoy assembling DIY (DO-IT-YOURSELF) products? "))
            + laborChoice
        )
        print("Score for all choices are: ", creativeChoice, stemChoice, laborChoice)

        return careerOutput(creativeChoice, stemChoice, laborChoice)


# def errorCheck(creativeChoice, stemChoice, laborChoice):
#     if creativeChoice.isdigit() and stemChoice.isdigit() and laborChoice.isdigit():
#     return careerOutput(creativeChoice, stemChoice, laborChoice)
#     else:
#     ("Restart the program lol")
#     return
