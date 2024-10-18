# In a list of array store even and odd numbers in new list and print
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
odd_numbers = []

for number in array:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# print sum of list
my_list = [1, 2, 3, 4, 5]

total_sum = sum(my_list)

print("Sum of the list:", total_sum)

# find duplicate element in a array and print in new array 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 4]

new_array = []
for number in array:
    if number in array:
        if number not in array:
           new_array.append(number)
    else:
        "invalide"
print(new_array)

array = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8]

duplicates = []
seen = set()

for number in array:
    if number in seen:
        if number not in duplicates:
            duplicates.append(number)
    else:
        seen.add(number)

print("Duplicate elements:", duplicates)

# largest & smallest number in a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)


# reverse a list.
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

# diff type (chatGPT)
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list) 

# add a new elements in tuple without using list constructor. I/P = (1,2,3,4,5)  O/P =(1,2,3,4,5,6,7,8,9,10).
original_tuple = (1, 2, 3, 4, 5)
new_elements = (6, 7, 8, 9, 10)
result_tuple = original_tuple + new_elements

print(result_tuple) 

# add a new elements in tuple without using list constructor . I/P =(“python”,”C”,”C++”)
# O/P = (“python”,”C”,”C++”,”java”,”java script”,”node js”).

original_tuple = ("python","c","c++")
new_elements = ("java script","node js" )
result_tuple = original_tuple + new_elements

print(result_tuple)