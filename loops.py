list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_data)

print(list_data[0])

# for number in list_data:
#     if number == 3:
#         print(number)
#     elif number > 3:
#         print("you passed 3")
#     else:
#         print("too soon")

# create a dictionary student_data
# iterate over dictionary
# using control flow - if elif else and for loop print all keys
# print all values
# print key with matching value

student_data = {
    "fname": "Angel",
    "lname": "Gelemerov",
    "age": 21,
}

for i in student_data.values():
    print(i)

for i in student_data.values():
    if i == "Angel":
        print(student_data.keys())
