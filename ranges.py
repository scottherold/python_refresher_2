# Fun with ranges

# In python 2, ranges were an object. Now they are a function

# if you only pass a single value to the range, it is the end value
# the start value will default to 0
# my_list = list(range(10))
# print(my_list)

# create lists of ranges with steps
even = list(range(0, 1000, 2))
odd = list(range(1, 1000, 2))

print(even)
print(odd)

# Python lists are very efficient
# These two lines will use the same amount of memory
range(0,100)
range(0,1000000000)

# Remember, strings are sequences and can be indexed
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

# ranges are also considered sequences and can be indexed
small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))

# accessing indexes, even in large range sequences, is very efficient
odd = range(1, 10000, 2)
print(odd)
print(odd[985])

sevens = range(7, 1000000, 7)
x = int(input("Please enter a positive number less than one million: "))
if x in sevens:
    print("{} is divisible by seven".format(x))

# you can also slice ranges
print(small_decimals)
my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

# These two for loops will print the same data
for i in my_range:
    print(i)

print('=' * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))