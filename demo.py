# multi-variable assignment

# multiple variables can be assigned the same value
a = b = c = d = 12
print(c)

# multiple variables can be assigned multiple values simultaneously
a, b = 12, 13
print(a, b)

# variable assignments go from right to left
a, b, = b, a
print("a is {}".format(a))
print("b is {}".format(b))