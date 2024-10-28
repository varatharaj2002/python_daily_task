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
# greeting()

# greet=outer_dec(greeting) ##decoratpor function assign

# greet()

greeting()



# class - blueprint

# class goa:
#     Name=""
#     Age=0
#     Place=""
#     ModeOfTravel=""

#     def beach(self):
#         print("beach relax....")

#     def party(self):
#         print("party.....")

# obj1=goa() #object creation


# obj1.Name="Sudharani"
# obj1.Age=23
# obj1.Place="pondy"
# obj1.ModeOfTravel="Train"
# obj1.beach()

# print(obj1.Age)


# constructor function
# self - current object values return

# class goa:
    
#     def _init_(self,Name,Age,Place,ModeOfTravel):
#         self.Name=Name
#         self.Age=Age
#         self.Place=Place
#         self.ModeOfTravel=ModeOfTravel
        
#     def get_func(self):
#         print("Name:",self.Name)
#         print("Age:",self.Age)
#         print("Place:",self.Place)
#         print("ModeOfTravel:",self.ModeOfTravel)

#     def set_name_func(self,Name):
#         self.Name=Name

#     def beach(self):
#         print("beach relax....")

#     def party(self):
#         print("party.....")


# obj1=goa("sudharani",21,"pondy","Train")

# print(obj1.Age)

# obj1.get_func()
# obj1.Name="Vardhu"
# obj1.get_func()

# obj1.set_name_func("sudharani")
# obj1.get_func()