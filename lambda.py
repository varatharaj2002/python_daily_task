# ANANYMOUS FUNCTION/LAMBDA FUNCTION  TASK

# Add Two Numbers
add = lambda x, y: x + y
result = add(5, 3)
print(result)

# Find the Maximum of Two Numbers
max_number = lambda x, y: x if x > y else y
result = max_number(10, 15)
print(result)

# Square a Number
square = lambda x: x ** 2
result = square(4)
print(result)

# Reverse a String
reverse_string = lambda s: s[::-1]
result = reverse_string("dom.....")
print(result)

# Check if a Number is Even
even = lambda x: x % 2 == 0 
result = even(10)
print(result)

# ...................................................
# RECURSION TASK:

# print 10 to 1.
def display(n):
    if n>0:
        print(n)
        display(n-1)
display(10)

# Print 1 to 10.
def print_numbers(n, limit):
    if n <= limit:
        print(n)
        print_numbers(n + 1, limit)
print_numbers(1, 10)

# Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(10):
    print(fibonacci(i))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

user_input = int(input("Enter a number: "))
if user_input < 0:
    print("Invalid input: Negative numbers do not have a factorial.")
elif user_input == 0:
    print("Factorial of 0 is 1.")
else:
    result = factorial(user_input)
    print("The factorial of" ,user_input, "is" ,result)





