# Write a Python program that asks the user to input a number and prints the reciprocal of that number. 
# Handle the exception if the user inputs zero 



# try:
#     number = float(input("Please enter a number: "))
#     if number == 0:
#         raise ValueError("Reciprocal of zero is undefined.")
#     reciprocal = 1 / number
#     print(f"The reciprocal of {number} is {reciprocal}.")
# except ValueError as e:
#     print(f"Error: {e}")
# except TypeError:
#     print("Error: Please enter a numeric value.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")    


# Write a program that reads a number from the user and prints its square. Use the else clause to print a success message
# try:
#     number = int(input("Enter a number: "))
#     square = number ** 2
# except ValueError:
#     print("Enter a valid number.")
# else:
#     print(square)
#     print("Success! The calculation was completed.")


# Modify the program in Task 3 to include a finally clause that prints a message regardless of whether an exception occurred or not
# try:
#     number = float(input("Enter a number: "))
#     square = number ** 2
# except ValueError:
#     print("Enter a valid number.")
# else:
#     print(square)
#     print("Success! The calculation was completed.")
# finally:
#     print("Thank you!")


# Write a function that raises a ValueError if the input number is negative
# def check_positive(number):
#     if number < 0:
#         raise ValueError("Input number must be positive!!!!!!!!!!!!!!!!!!!!.")
#     return number

# try:
#     user_input = int(input("Enter a positive number: "))
#     check_positive(user_input)
#     print("You entered:", user_input)
# except ValueError as e:
#     print(e)

# Write a program that repeatedly asks the user for a number and handles exceptions. The program should continue asking until a valid number is entered.
# while True:
#     try:
#         user_input = int(input("Enter a number: "))
#         break 
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# print("You entered a valid number:",user_input)



