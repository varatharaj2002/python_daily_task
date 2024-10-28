# decorator
# closure funcytion

# def outer():
#     def inner():
#         print("success")
#     return inner

# print(outer())

# def outer_dec(fun):
#     def inner_dec():
#         print("thanks for entering .....")
#         fun()
#         print("bye....")

#     return inner_dec

# @outer_dec #decortor function
# def greeting():
#     print("Welcome to my Home...")

# greet=outer_dec(greeting) ##decoratpor function assign

# greet()

# greeting()

name = input("Enter your name:")
cmp = input("Enter your company name:")
points = input("Your suggestion:")
def outer_dec(fun):
    def inner_dec():
        print("welcome", name)
        fun()
        print("review",points)
        print("Congratulations, all the best for your future",name)
    return inner_dec  

@outer_dec #decortor function
def greeting():
    print(f"thx for entering {name} into {cmp}")  
greeting()