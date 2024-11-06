# 1.create student class and possible functions and attributes. using contructor funct,set and get function

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