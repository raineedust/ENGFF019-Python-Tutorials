# # 1 T7-Q1.py

# total = 0
# print("This program prints a sum of number series.")
# value = int(input("How many numbers do you want?"))

# for i in range(value):
#     total = total + (i + 1)

# print("Sum of the number series [ 1 to", value, "] is:", total)

# # 2 T7-Q2.py

# total = 0
# count = 0
# print("This program prints a sum of number series.")
# value = input("How many numbers do you want?")

# while count <= 2:
#     if value.isdigit:
#         if int(value) >= 0:
#             for i in range(int(value)):
#                 total = total + (i + 1)
#             break
#         else:
#             print("Please retry and enter a positive integer number.")
#             count = count + 1
#     else:
#         print("Please retry and enter a positive integer number.")
#         count = count + 1


# if count == 3:
#     print("The program is terminated. You've run out of chances.")

# print("Sum of the number series [ 1 to", value, "] is:", total)

# 3

total = 0
count = 0
print("This program prints a sum of number series.")
value = input("How many numbers do you want?")

while count <= 2:
    if value.isdigit:
        if int(value) >= 0:
            for i in range(int(value)):
                total = total + (i + 1)
            option = input("Press Y to continue, or any key to exit :")
            print()
            if option.upper() == "Y":
                continue
            else:
                print("Thank you for using our service.")
                count = count + 1
                break
        else:
            print("Please retry and enter a positive integer number.")
            count = count + 1
    else:
        print("Please retry and enter a positive integer number.")
        count = count + 1


if count == 3:
    print("The program is terminated. You've run out of chances.")

print("Sum of the number series [ 1 to", value, "] is:", total)
