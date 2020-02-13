# Fun with lists!

# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of life"]

parrot_list.append("A Norwegian Blue") # append adds a new list item
for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd # lists can be combined with a simple '+' operator

# sort is a native method to lists
# sort orders a list ascending by default
# numbers.sort()

# sorted() mutates (creates a new, modified version) of the list
# you cannot use print(numbers.sort())
# this is because list methods overwrite the original list
numbers_in_order = sorted(numbers)

print(numbers_in_order)

# This will print that the lists are not equal
if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

# this will print that the lists are not equal
# this is because .sort() does not instantiate a new list
# therefore, the operator is comparing the original list
if numbers_in_order == numbers.sort():
    print("The lists are equal")
else:
    print("The lists are not equal")

# this will print the lists are equal
# this is because, like when creating the numbers_in_order variable
# Python mutates (creates a new modified) list
if numbers_in_order == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")