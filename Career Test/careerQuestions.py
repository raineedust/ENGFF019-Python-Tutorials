# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553


from careerResult import careerOutput


def careerInput(startTest):

    while startTest == 1:
        print(", please enter either (1) if you agree, or (2) if you disagree")

        creativeChoice = int(input("Would you enjoy designing a magazine cover?"))
        creativeChoice = (
            int(input("Would you enjoy taking pictures of nature?")) + creativeChoice
        )

        stemChoice = int(input("Do scientific experiments interest you?"))
        stemChoice = (
            int(input("Does researching a new medicine sound attractive to you?"))
            + stemChoice
        )

        laborChoice = int(input("Would you enjoy installing a hardwood floor?"))
        laborChoice = (
            int(input("Do you enjoy assembling DIY (DO-IT-YOURSELF) products"))
            + laborChoice
        )

        if startTest == 2:
            print("Thank you for your time", "!")
        else:
            print("Error, please enter either (1) or (2)")
        startTest = startTest + 1
        careerInput(creativeChoice, stemChoice, laborChoice)
