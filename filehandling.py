

file1 = open('file1.txt', 'w')
file1.write("bro kari kada bhai dhana bhai!!!")
file1.close()

file1 = open('file1.txt', 'r')
text = file1.read()
file1.close()

# for i in text:
file2 = open('file2.txt', 'w')
file2.write(text)
file2.close()

print("Text transferred from file1 to file2.")

# # Create and write to the first file
# with open('file1.txt', 'w') as file1:
#     file1.write('This is some text.')

# # Read from the first file and write to the second file
# with open('file1.txt', 'r') as file1:
#     content = file1.read()

# with open('file2.txt', 'w') as file2:
#     file2.write(content)

# print("Text copied from file1.txt to file2.txt.")

# for i in text(1,2):
#     # return i
#     print(i)
