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

# name = input("Enter your name:")
# cmp = input("Enter your company name:")
# points = input("Your suggestion:")
# def outer_dec(fun):
#     def inner_dec():
#         print("welcome", name)
#         fun()
#         print("review",points)
#         print("Congratulations, all the best for your future",name)
#     return inner_dec  

# @outer_dec #decortor function
# def greeting():
#     print(f"thx for entering {name} into {cmp}")  
# greeting()

# greet=outer_dec(greeting) ##decoratpor function assign

# greet()

# greeting()



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

# create student class and possible functions and attributes. using contructor funct,set and get function

class Student:
    def __init__(self, name, age, student_id):
        self._name = name  # Private attribute
        self._age = age    # Private attribute
        self._student_id = student_id  # Private attribute

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Simple validation
            self._age = age
        else:
            raise ValueError("Age must be a positive integer.")

    # Getter for student_id
    def get_student_id(self):
        return self._student_id

    # Setter for student_id
    def set_student_id(self, student_id):
        self._student_id = student_id

    # Method to display student information
    def display_info(self):
        return f"Name: {self._name}, Age: {self._age}, Student ID: {self._student_id}"

# Example usage
if __name__ == "__main__":
    student1 = Student("Alice", 20, "S12345")
    print(student1.display_info())

    student1.set_age(21)
    print(student1.display_info())

# 2. Create a  class called laptop. Create  a following variables and functions . 
  		# Var = price, processor, ram
# Create object as Lenovo, HP, Dell

class Laptop:
    def __init__(self, brand, price, processor, ram):
        self.brand = brand  # Brand of the laptop
        self.price = price  # Price of the laptop
        self.processor = processor  # Processor type
        self.ram = ram  # Amount of RAM

    # Getter methods
    def get_price(self):
        return self.price

    def get_processor(self):
        return self.processor

    def get_ram(self):
        return self.ram

    # Setter methods
    def set_price(self, price):
        self.price = price

    def set_processor(self, processor):
        self.processor = processor

    def set_ram(self, ram):
        self.ram = ram

    # Method to display laptop information
    def display_info(self):
        return (f"Brand: {self.brand}, Price: ${self.price}, "
                f"Processor: {self.processor}, RAM: {self.ram} GB")

# Creating laptop objects
if __name__ == "__main__":
    lenovo = Laptop("Lenovo", 1200, "Intel i7", 16)
    hp = Laptop("HP", 1000, "Intel i5", 8)
    dell = Laptop("Dell", 1500, "Intel i9", 32)

    # Displaying information about the laptops
    print(lenovo.display_info())
    print(hp.display_info())
    print(dell.display_info())

# 3.create class called Kodaikanal.and create all the possible variables and functions

class Kodaikanal:
    def __init__(self, attractions, average_temperature, activities, local_cuisine):
        self.attractions = attractions  # List of tourist attractions
        self.average_temperature = average_temperature  # Average temperature in Celsius
        self.activities = activities  # List of activities to do
        self.local_cuisine = local_cuisine  # List of local cuisines

    # Getter methods
    def get_attractions(self):
        return self.attractions

    def get_average_temperature(self):
        return self.average_temperature

    def get_activities(self):
        return self.activities

    def get_local_cuisine(self):
        return self.local_cuisine

    # Setter methods
    def set_attractions(self, attractions):
        self.attractions = attractions

    def set_average_temperature(self, temperature):
        self.average_temperature = temperature

    def set_activities(self, activities):
        self.activities = activities

    def set_local_cuisine(self, cuisine):
        self.local_cuisine = cuisine

    # Method to display information about Kodaikanal
    def display_info(self):
        return (f"Kodaikanal:\n"
                f"Attractions: {', '.join(self.attractions)}\n"
                f"Average Temperature: {self.average_temperature}°C\n"
                f"Activities: {', '.join(self.activities)}\n"
                f"Local Cuisine: {', '.join(self.local_cuisine)}")

# Example usage
if __name__ == "__main__":
    attractions = ["Kodaikanal Lake", "Pillar Rocks", "Bear Shola Falls"]
    activities = ["Boating", "Trekking", "Sightseeing"]
    local_cuisine = ["Dosa", "Idli", "Vada"]

    kodaikanal = Kodaikanal(attractions, 18, activities, local_cuisine)

    # Displaying information about Kodaikanal
    print(kodaikanal.display_info())
# .............................................................................
# Create a base class called shape withe method area that return 0 .
# create a derived class called rectangle that inherit from shape and overrides the area method to 
# calculate and return the area of a rectangle.
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create a Shape object
shape = Shape()
print("Area of shape:", shape.area())  # Output: Area of shape: 0

# Create a Rectangle object
rectangle = Rectangle(5, 10)
print("Area of rectangle:", rectangle.area())  # Output: Area of rectangle: 50


# create a base class called person with constructor that takes a name as a parameter .
#  Create a derived called student that inherits from  person has constructor that takes a parameter called grade. 
# Write a method in student to display name and grade of student . Use super keywords to achieve this.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        # Initialize the name attribute from the Person class
        super().__init__(name)
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

# Create a Student object
student = Student("Alice", "A")
student.display_info()  # Output: Name: Alice, Grade: A

# create a base class called vehicle with a method start that print " vehicle started" 
# create a derived class called car that inherits from vehicle and overrides the start method to print " car started”.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")

# Create a Vehicle object
vehicle = Vehicle()
vehicle.start()  # Output: Vehicle started

# Create a Car object
car = Car()
car.start()  # Output: Car started

# create a base class called employee with properties name and salary . 
# Create a derived class called manager that inherits from employee and adds a property department .
#  Write a method in manager to display the name , salary , and department of the manager.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Initialize properties of the base class Employee
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

# Create a Manager object
manager = Manager("John Doe", 80000, "Sales")
manager.display_info()

# Name: dom
# Salary: 80000
# Department: Sales

# at prints "Animal makes sounds" .create a derived class called dog that inherits from animals and overrides 
# the sounds methods to print "dog barks " .create a another function derived class bird that 
# inherits from animal and overrides sound method to print " birds print"
class Animal:
    def sound(self):
        print("Animal makes sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Bird(Animal):
    def sound(self):
        print("Birds sing")

# Create an Animal object
animal = Animal()
animal.sound()  # Output: Animal makes sounds

# Create a Dog object
dog = Dog()
dog.sound()  # Output: Dog barks

# Create a Bird object
bird = Bird()
bird.sound()  # Output: Birds sing

# ..................................ENCAPSULATION.............................................

# Class company with constructor with private varible.With variable name as method.
# To access that varibale.Protected varibale can access child class.
class Company:
    def __init__(self, name, revenue):
        self.__name = name  # Private variable
        self._revenue = revenue  # Protected variable

    # Method to access the private variable __name
    def get_name(self):
        return self.__name

    # Method to access the protected variable _revenue
    def get_revenue(self):
        return self._revenue

class ChildCompany(Company):
    def __init__(self, name, revenue, location):
        # Initialize the base class constructor
        super().__init__(name, revenue)
        self.location = location

    # Method to access the protected variable _revenue in the child class
    def display_details(self):
        print(f"Company Name: {self.get_name()}")
        print(f"Revenue: {self.get_revenue()}")
        print(f"Location: {self.location}")

# Create an object of Company class
company = Company("TechCorp", 1000000)
# Access private variable using the public method
print(company.get_name())  # Output: TechCorp
print(company.get_revenue())  # Output: 1000000

# Create an object of ChildCompany class
child_company = ChildCompany("TechCorp Ltd.", 500000, "New York")
child_company.display_details()


# Create a base class called shape withe method area that return 0 .
# create a derived class called rectangle that inherit from shape and overrides 
# the area method to calculate and return the area of a rectangle.

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an object of Shape class
shape = Shape()
print(f"Area of shape: {shape.area()}")  # Output: Area of shape: 0

# Create an object of Rectangle class
rectangle = Rectangle(5, 10)
print(f"Area of rectangle: {rectangle.area()}")  # Output: Area of rectangle: 50

# create a base class called person with constructor that takes a name as a parameter . 
# Create a derived called student that inherits from  person has constructor that takes a parameter called grade.
# Write a method in student to display name and grade of student . Use super keywords to achieve this.
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        # Use super() to call the constructor of the base class (Person)
        super().__init__(name)
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")

# Create a Student object
student = Student("dom", "A")
student.display_info()

# Name: dom
# Grade: A

# create a base class called vehicle with a method start that print " vehicle started" create a derived 
# class called car that inherits from vehicle and overrides the start method to print " car started”.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")

# Create an object of Vehicle class
vehicle = Vehicle()
vehicle.start()  # Output: Vehicle started

# Create an object of Car class
car = Car()
car.start()  # Output: Car started

# create a base class called employee with properties name and salary . 
# Create a derived class called manager that inherits from employee and adds a property department .
# Write a method in manager to display the name , salary , and department of the manager.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Initialize the properties from the base class (Employee)
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

# Create a Manager object
manager = Manager("dom", 80000, "Sales")
manager.display_info()
