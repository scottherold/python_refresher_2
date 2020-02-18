# multi-value assignment with tuples

# tuple creation
# tuples can nest tuples
imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
    (4, "Kentish Town Waltz")
)

# tuple unpacking (like object destructing in JS)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

# something similar can be done with lists
metallica = ["Ride the Lightning", "Metallica", 1984]

# Add 'Rock' the the list
metallica.append("Rock")

# list unpacking
# this will error, because you are not assigning a variable to 'Rock'
# with unpacking, all variables must be assigned
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)