# 1Create a Person class and a Student class that inherits from Person .
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the __init__ method of the superclass (Person)
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        # Extend the introduce method to include student ID
        super().introduce()
        print(f"My student ID is {self.student_id}.")

# Create a Person instance
person = Person("Dom", 21)
person.introduce()

# Create a Student instance
student = Student("buu", 20, "S12345")
student.introduce()

# 2.Create a class Animal, a Mammal class that inherits from Animal, and a Dog class that inherits from Mammal.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("This animal makes a sound.")

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

    def speak(self):
        print("This mammal makes a sound.")

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Woof! Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")

animal = Animal("Generic Animal")
animal.speak()

mammal = Mammal("Generic Mammal")
mammal.speak()

dog = Dog("Buddy", "Golden Retriever")
dog.speak()
dog.fetch()

# 3.Create a class Vehicle and two classes Car and Bike that inherit from Vehicle.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"The {self.brand} {self.model} is starting.")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def start(self):
        print(f"The car {self.brand} {self.model} with {self.seats} seats is starting.")

class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def start(self):
        print(f"The bike {self.brand} {self.model} ({self.bike_type} bike) is starting.")

vehicle = Vehicle("Generic", "ModelX")
vehicle.start()

car = Car("Toyota", "Corolla", 5)
car.start()

bike = Bike("Yamaha", "YZF-R3", "Sport")
bike.start()


# 4.Create a Teacher class, a Student class that both inherit from Person, and an Assistant class that inherits from both.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject}.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super().introduce()
        print(f"My student ID is {self.student_id}.")

class Assistant(Teacher, Student):
    def __init__(self, name, age, subject, student_id):
        Teacher.__init__(self, name, age, subject)
        Student.__init__(self, name, age, student_id)

    def introduce(self):
        super().introduce()
        print("I am also an assistant.")

# Create a Teacher instance
teacher = Teacher("Mr. varatha", 21, "Math")
teacher.introduce()

# Create a Student instance
student = Student("nandaa", 12, "S12345")
student.introduce()

# Create an Assistant instance
assistant = Assistant("ajay", 18, "Physics", "A67890")
assistant.introduce()


# ....................................................................................
# Class a having  display function and Constructor class b having  display function create obj for a . Create a obj for b and access a constructor by using super keywords.
class ClassA:
    def __init__(self):
        print("Constructor of ClassA")

    def display(self):
        print("Display from ClassA")

class ClassB(ClassA):
    def __init__(self):
        # Call the constructor of ClassA using super()
        super().__init__()
        print("Constructor of ClassB")

    def display(self):
        print("Display from ClassB")

# Create an object for ClassA
obj_a = ClassA()
obj_a.display()

# Create an object for ClassB
obj_b = ClassB()
obj_b.display()


# Class c having display function have to inherit class a and class b constructor.
class ClassA:
    def __init__(self):
        print("Constructor of ClassA")

    def display(self):
        print("Display from ClassA")

class ClassB:
    def __init__(self):
        print("Constructor of ClassB")

    def display(self):
        print("Display from ClassB")

class ClassC(ClassA, ClassB):
    def __init__(self):
        # Call constructors of both ClassA and ClassB
        ClassA.__init__(self)
        ClassB.__init__(self)
        print("Constructor of ClassC")

    def display(self):
        # Optionally call display methods from both ClassA and ClassB
        print("Display from ClassC")

# Create an object for ClassC
obj_c = ClassC()
obj_c.display()

# .......................................................................................