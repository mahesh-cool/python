#literal assignment
first = "mahesh"
last = "S"

#  prine (type(first))
# print(type(first)==str)
# print(isinstance(first, str))

#constructor function
# pizza =str("pepperoni")
# print (type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza, str))

#concatenation
# fullname = first + "  " + last
# print(fullname)

# fullname += "!"
# print(fullname)

#Multiple Lines
multiline = '''
Hey, How are you ?
 
 I was just checking in. 

             All good?
             '''
print(multiline)

#Escaping special Characters
sentence = 'I\'m back at work!\t Hey!\n\n Where\'s this at \\located'
print(sentence) 

#string Methods
print(first)
print(first.lower())
print(first.upper())
print(first)
print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)
print(len(multiline))
print(len(multiline))
multiline +=""
multiline = "             "+multiline
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# build a menu
title = "menu".upper()
print(title.center(30, "+"))
print("Cofee".ljust(16,".") + "$1".rjust(4))
print("muffin".ljust(16,".") + "$3".rjust(4))
print("Cheescake".ljust(16,".") + "$4".rjust(4))\

print("")

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some methods return boolean data
print(first.startswith("m"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#numberic data types
#integer type
price =100
best_price =int(80)
print(type(price))
print(isinstance(best_price,int))


#float type
gpa = 3.28
y = float(1.4)
print(type(gpa))

#complex type
comp_value = 5+3j

print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built in fuction for numbers

print(abs(gpa))

print(round(gpa))

print(round(gpa,2))


#math importing and working on it

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number
zipcode = "600053"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
#zip_value = int(New York")
