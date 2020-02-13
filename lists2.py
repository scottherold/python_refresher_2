# More fun with lists

# List constructors -- aka, lists with empty brackets
# list_1 = []
# list_2 = []

# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))

# if list_1 == list_2:
#     print("The lists are equal")

# print(list("The lists are equal"))


# when you assign a variable to equal an existing variable
# an updates to the new variable, will also up the existing variable
# this is because both variable point to the same list when assigned
even = [2, 4, 6, 8]

# another_even = even # commented out for demonstration purposes

# if you use a list constructor, a new list is instantiated
# this is instead of both varaibles pointing the the same list
# another_even = list(even) # commented out for demonstration purposes

# if the existing list is passed through the sorted() function
# it will also mutate and instantiate a new list
another_even = sorted(even, reverse=True)

# this will return True
# this is because both variables point to the same list when assigned
print(another_even is even)
another_even.sort(reverse=True)

# this will print [8, 6, 4, 2] if an existing list is assigned
# this is because both variables point to the same list when assigned
# however, if another_even is assigned to a newly constructed list
# using the existing list OR mutated from the existing list
# with something like the sort() function this will print [2, 4, 6, 8]
# this is because a new list is mutated from the existing list and
# has a separate pointer
print(even)

# You can create a list of lists
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)