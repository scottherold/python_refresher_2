# Create a list of items (you may use either strings or numbers)
# then create an iterator using the iter() function.

# Use a for loop to loop "n" times, where n is the number of items in
# your list. Each time round the loops, use next() on your list to
# to print the next item

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
number = iter(numbers)

for i in range(0, len(numbers)):
    print(next(number))