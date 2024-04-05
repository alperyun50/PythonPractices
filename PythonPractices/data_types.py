# String data type

# Literal assignment
first = "Dave"
last = "Gray"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concat
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to string
decade = str(1980)
print(decade)

# Multiple lines
multiline = '''
Hey, how are you?

i was just checking in.

All good?

'''
print(multiline)

# Escaping special caracters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                           "
multiline = "                  " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])
print(first)

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(myvalue)
print(x)

# Numeric data types

# Integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in Functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
print(zip_value)