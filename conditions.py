#check even or odd
number =int(input("enter a number:"))

if number % 2==0:
    print(number," is even number")
else:
    print(number,"is odd number")

#check if a number is divisible by 5
number =int(input("enter a number:"))

if number % 5==0:
    print(number," is divisible by 5")
else:
    print(number,"is not divisible by 5")

#print larger number

numA = int(input("enter numA:"))
numB = int(input("enter numB:"))

if numA>numB:
    print("numA is larger number:",numA)
else:
    print("numB is larger number:",numB)

#Check if a string contains a specific substring.
string = "Hello, world!"
substring = "world"

if substring in string:
    print("Substring found.")
else:
    print("Substring not found.")

#Check if a number is between 1 and 10.
value = int(input("enter a number:"))
if 1 <= value <= 10:
    print("The number is between 1 and 10.")
else:
    print("The number is not between 1 and 10.")

#Check if a character is a vowel.

#Check if a person is eligible to vote (age >= 18).
age = int(input("enter your age:"))
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

#Determine if a year is a leap year.

#Check if a given number is a multiple of 3 and 7.
number = int(input("enter a number:"))
if number % 3 == 0 and number % 7 == 0:
    print(f"{number} is a multiple of both 3 and 7.")
else:
    print(f"{number} is not a multiple of both 3 and 7.")

#Check if a person is a teenager (age between 13 and 19).
age = int(input("enter your age:"))
if 13 <= age <= 19:
    print("The person is a teenager.")
else:
    print("The person is not a teenager.")

#Find the largest of three numbers.

#Check if a number is divisible by both 5 and 11.
number = int(input("enter a number:"))
if number % 5 == 0 and number % 11 == 0:
    print(f"{number} is divisible by both 5 and 11.")
else:
    print(f"{number} is not divisible by both 5 and 11.")

#Determine the grade based on marks.
mark = int(input("enter your mark here:"))
if mark >= 90:
    grade = 'A'
elif mark >= 80:
    grade = 'B'
elif mark >= 70:
    grade = 'C'
elif mark >= 60:
    grade = 'D'
elif mark >= 50:
    grade = 'E'
else:
    grade = 'F'
print("the grade for",mark,"mark is",grade)

#Check if a number is positive and even.
number = int(input("enter a number :"))
if number > 0 and number % 2 == 0:
    print( number,"is positive and even.")
else:
    print( number,"is not positive and even.")

#Check if a number lies between 10 and 20.
#Determine if a string is empty.

#check the number is positive or negative
numbers = int(input("enter a number:"))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")