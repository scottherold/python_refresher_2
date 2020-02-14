# more fun with ranges
decimals = range(0, 100)
my_range = decimals[3:40:3]
print(my_range == range(3, 40, 3))

# This will print ture
# The reason is, both ranges with have the same sequence of values
# Remember, ranges end is exclusive, the both of these ranges will equal
# [0, 2, 4]
print(range(0, 5, 2) == range(0, 6, 2))

# display to demonstrate
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

# the same is true with slices
r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)

print('=' * 50)
for i in range(99, 0, -2):
    print(i)

print('=' * 50)

# this will print true
print(range(0, 100)[::-2] == range(99, 0, -2))

# This will not print, because it is a negative step and the
# range start is lower than its end. This works with the slice
# but the iterator does not know how to handle this syntax
for i in range(0, 100, -2):
    print(i)

# You can slice strings backward too
backString = "eugaugnal lufrewop yrev a si nothyP"
print(backString[::-1])

# You can run the iterator through a slice
r = range(0, 10)
for i in r[::-1]:
    print(i)