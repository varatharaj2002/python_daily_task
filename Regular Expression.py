import re

# ^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$
# r'^[\w\.-]+@[\w\.-]+\.\w+$'
# email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'D

# Regular expression for validating an email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def check_email():
    email = input("Enter your email ID: ")
    if re.match(email_pattern, email):
        print("Your email ID is correct.")
    else:
        print("Please enter a correct email ID.")


check_email()
