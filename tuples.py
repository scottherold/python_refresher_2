# learning tuples

# while tuples are designated as a sequence within paranthesis
# they do not have to be typed that way

# this is a tuple
t = "a", "b", "c"
print(t)

# this is not a tuple, but three separate strings
print("a", "b", "c")

# this is a tuple
# you need to put brackets around the sequence to use a tuple
print(("a", "b", "c"))

# CSV values
welcome = "Welcome to my Night", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# accessing tuples
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# this will error because values in a tuple cannot be mutated
# metallica[0] = "Master of puppets"

# tuples actually support indexing and slicing
# this can be used to re-assign a variable of the same type
# for example, here we access the tuple, and change the second index
# to a new string
imedla = imelda[0], "Imelda May", imelda[2]
print(imelda)

# here is a list to illustrate the difference
metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)

# you can directly reassign a value in the list
metallica2[0] = "Master of Puppets"
print(metallica2)