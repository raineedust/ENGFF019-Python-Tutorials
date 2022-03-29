# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553

creativeCareer = ["Photographer", "UI Designer", "Makeup Artist"]
stemCareer = ["Software Developer", "Scientist", "Doctor"]
laborCareer = ["Custodian", "Carpenter", "Plumber"]


def careerOutput(creativeChoice, stemChoice, laborChoice):
    for i in creativeCareer:
        if creativeChoice >= 3:
            print("Based on your answers, we think you'd enjoy being a", i)
    for i in stemCareer:
        if stemChoice >= 3:
            print("Based on your answers, we think you'd enjoy being a", i)
    for i in laborCareer:
        if laborChoice >= 3:
            print("Based on your answers, we think you'd enjoy being a", i)
