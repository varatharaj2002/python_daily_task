# Square all numbers in a list
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# Convert all strings in a list to uppercase
def to_uppercase(s):
    return s.upper()
strings = ["varatha", "dom"]
uppercase_strings = list(map(to_uppercase, strings))
print(uppercase_strings)

# Add 10 to each number in a list
def add_ten(x):
    return x + 10
numbers = [1, 2, 3, 4]
updated_numbers = list(map(add_ten, numbers))
print(updated_numbers)

# Double each number in a list
def double(x):
    return x * 2
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)

# Capitalize the first letter of each string in a list
def capitalize_first(s):
    return s.capitalize()
strings = ["hello", "world", "python"]
capitalized_strings = list(map(capitalize_first, strings))
print(capitalized_strings)

# Filter out even numbers from a list
def odd(x):
    return x % 2 != 0
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(odd, numbers))
print(odd_numbers)

# Filter out words shorter than 4 characters
def shorter(word):
    return len(word) >= 4

words = ["iphone", "is", "chapri", "siuu", "bye"]
filtered_words = list(filter(shorter, words))
print(filtered_words)

# Filter out numbers greater than 10
def greater_than(x):
    return x <= 10

numbers = [5, 12, 8, 21, 3, 10]
filtered_numbers = list(filter(greater_than, numbers))
print(filtered_numbers)

# Filter out strings containing the letter 'a'
def contains_a(s):
    return 'a' not in s

strings = ["apple", "dom", "siuu", "hai"]
filtered_strings = list(filter(contains_a, strings))
print(filtered_strings)

# Filter out numbers that are not divisible by 3
def is_divisible_by_3(x):
    return x % 3 == 0
numbers = [1, 3, 4, 6, 7, 9, 10, 12]
filtered_numbers = list(filter(is_divisible_by_3, numbers))
print(filtered_numbers)

# Filter out negative numbers from a list
def is_negative(x):
    return x >= 0
numbers = [-5, 3, 0, -2, 7, -1, 4]
filtered_numbers = list(filter(is_negative, numbers))
print(filtered_numbers)

# Find the product of all numbers in a list
from functools import reduce
def multiply(x, y):
    return x + y
numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)
print(product)  # Output: 24

# Concatenate a list of strings
from functools import reduce

def concatenate(s1, s2):
    return s1 + s2

strings = ["Hello", " ", "world", "!"]
result = reduce(concatenate, strings)
print(result)  # Output: 'Hello world!'

# Compute the sum of squares of numbers in a list
from functools import reduce

def square(x):
    return x ** 2

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
sum_of_squares = reduce(add, squared_numbers)
print(sum_of_squares)  # Output: 30

# Compute the factorial of a number using reduce
from functools import reduce

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

result = factorial(5)
print(result)  # Output: 120


