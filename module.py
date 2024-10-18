# import random
# mylist = ["apple", "varatha", "dom", "hello"]
# # print(random.choice(mylist))
# # print(random.sample(mylist,2))

# random.shuffle(mylist)

# print(mylist)

import random

mylist = [1, 2, 3, 4, 5,]

while True:
    correct_number = random.choice(mylist)
    print("Try to guess it!")

    while True:
        user_input = input("Guess a number from 1 to 5: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == correct_number:
                print("Your guessing is correct!")
                break
            else:
                print("Your guessing is wrong. Try again.")
        else:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
