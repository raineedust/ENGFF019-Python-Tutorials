# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553

import mainModule
import careerResult


def Check(startTest):

    while startTest == 1:
        print(name, ", please enter either (1) if you agree, or (2) if you disagree")

        i = int(input("Would you enjoy designing a magazine cover?"))
        i = input("Would you enjoy taking pictures of nature?") + i

        j = int(input("Do scientific experiments interest you?"))
        j = input("Does researching a new medicine sound attractive to you?") + j

        k = int(input("Would you enjoy installing a hardwood floor?"))
        k = input("Do you enjoy assembling DIY (DO-IT-YOURSELF) products") + k

        if startTest == 2:
            print("Thank you for your time", name, "!")
        else:
            print("Error, please enter either (1) or (2)")
        startTest = startTest + 1


careerResult()
