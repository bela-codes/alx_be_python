# number = int(input("Enter the size of the pattern: "))

# # i = 1
# # while i <= number:
# #     print("*")
# #     i += 1

# for j in range(number):
#     print("*")
#     for k in range(number):
#         print("*", end="")

# pattern_drawing.py

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Validate input
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Move to next line after each row
        row += 1
