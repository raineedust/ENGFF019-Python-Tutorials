# Anthony Saopa Phiri 20401485
# Tan Jin Yi 20396553


def error(firstName, lastName):
    if firstName.isalpha() and lastName.isalpha():
        name = firstName + " " + lastName
        return name
    else:
        return "Error!,name should be only letters\n"
