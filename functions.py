# input(int("enter a number:"))
def square(number):
    return number ** 2

# Example usage
result = square(5)
print("The square of 5 is:", result)

# Calculate Area of Rectangle
def calculate_area(length, width):
    return length * width

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_area(length, width)

# Output the result
print(f"The area of the rectangle is: {area}")

# Check Even or Odd
num = int(input("Enter a number: "))
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(num)
print(result)

# Check Prime Number
num = int(input("Enter a positive integer: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Reverse a String
user_input = input("Enter a string: ")
def reverse_string(s):
    return s[::-1]

reversed_string = reverse_string(user_input)

print(f"The reversed string is: {reversed_string}")


def count_characters(input_string):
    return len(input_string)

# Example usage
text = "Hello, World!"
character_count = count_characters(text)
print(f"The number of characters is: {character_count}")

input = input("enter a char:")
def char(new_char):
    return len(new_char)