def errorCheck(value):
    if value.isdigit() == True:
        if int(value) >= 1 and int(value) <= 2:
            return
