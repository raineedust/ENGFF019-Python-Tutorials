# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553


creativeCareer = ["Photographer", "UI Designer", "Makeup Artist"]
stemCareer = ["Software Developer", "Scientist", "Doctor"]
laborCareer = ["Custodian", "Carpenter", "Plumber"]


def careerOutput(creativeChoice, stemChoice, laborChoice):
    if creativeChoice + stemChoice + laborChoice > 0:
        for i in creativeCareer:
            if creativeChoice > stemChoice or creativeChoice > laborChoice:
                print("Based on your answers, we think you'd enjoy being a", i)
        for i in stemCareer:
            if stemChoice > creativeChoice or stemChoice > laborChoice:
                print("Based on your answers, we think you'd enjoy being a", i)
        for i in laborCareer:
            if laborChoice > creativeChoice or laborChoice > stemChoice:
                print("Based on your answers, we think you'd enjoy being a", i)
    else:
        print(
            "Unfortunately, we do not have suitable careers based on your answers. We will keep improving on the test in the future!"
        )
