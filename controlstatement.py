# Print numbers from 1 to 10, but stop when the number is 5.
for number in range(1, 11):
    if number == 5:
        break
    print(number) 

# Find the first negative number in a list.

# Iterate over a list and stop if you encounter a zero.
numbers = [1, 2, 3, 0, 5, 6, 7]

for number in numbers:
    if number == 0:
        print("Encountered zero, stopping iteration.")
        break
    print(number)

# Print numbers from 1 to 10, skipping 5
for number in range(1, 11):
    if number == 5:
        continue  # Skip the number 5
    print(number)

# Print only even numbers from 1 to 10. 
for number in range(1, 11):
    if number % 2 != 0: 
        continue  
    print(number)

# Print characters of a string, skipping vowels
string = "Hello, World!"
vowels = "aeiouAEIOU"  # Define vowels to skip

for char in string:
    if char in vowels:
        continue 
    print(char, end='')

# Iterate over numbers from 1 to 20, but skip multiples of 3.
for number in range(1, 21):
    if number % 3 == 0:
        continue  
    print(number)

# Iterate over a list and use pass for future implementation.

# Iterate over numbers from 1 to 10, skip 5 and stop at 8.
for number in range(1, 11):
    if number == 5:
        continue  
    if number == 8:
        break  
    print(number)

# Print only odd numbers from 1 to 10, but use pass for even numbers.
for number in range(1, 11):
    if number % 2 == 0: 
        pass 
    else:
        print(number) 

# Iterate over a list, skip negatives, print positives, stop at zero.
numbers = [3, -1, 5, 0, 7, -3, 2]

for number in numbers:
    if number < 0:
        continue  # Skip negative numbers
    if number == 0:
        break  # Stop at zero
    print(number)  # Print positive numbers

# Skip the first half of a list, process the second half, use pass for future.

# Get a input from user like number until user enter zero after that have to print the product of numbers.
product = 1  # Initialize product
count = 0  # To check if at least one number is entered

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop if the user enters zero
    
    product *= number  # Multiply the current number to the product
    count += 1  # Increment the count of numbers entered

# Check if any number was entered before zero
if count > 0:
    print("The product of the numbers entered is:", product)
else:
    print("No numbers were entered.")

# Get a input from user like number until user enter negative number after that have to print the sum of numbers.


# ------------------------------------------------------------------------------------------------------------

# In a paragraph replace a “is” with “was” . then count no of “a” in a paragraph.
paragraph = "This is a simple paragraph that is meant to demonstrate the task. It is important to be clear."

# Replace 'is' with 'was'
modified_paragraph = paragraph.replace(" is ", " was ")

# Count the number of 'a' in the modified paragraph
a_count = modified_paragraph.lower().count('a')

# Print the results
print("Modified Paragraph:")
print(modified_paragraph)
print("Number of 'a' in the paragraph:", a_count)

# get a input from user check its a Email Id.
email = input("Enter an email address: ")
if "@" in email and email.count("@") == 1 and "." in email.split("@")[1]:
    print("The email address is valid.")
else:
    print("The email address is not valid.")

# get a input from user also check  its valid password.
password = input("Enter a password: ")
if (len(password) >= 8):
    print("The password is valid.")
else:
    print("The password is not valid. It must be at least 8 characters.")

# login task - get input from user name & password its align with your previous data.throw a login successful message.otherwise its a Invalid input.
correct_username = "user123"
correct_password = "Password@123" 

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid input.")

