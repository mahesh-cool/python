def hello_world():# definition for hello
    print("Hello world!")

hello_world()

# def sum(num1,num2):
#     print(num1 + num2)

def sum(num1,num2):
    if (type(num1) is not int or  type(num2) is not int):
        return
    return num1 + num2

total = sum("a",2) #since a is not an integer output will be none
print(total)

# sum(2,3)
# sum(1,7)# add both numbers 
#  total = sum() #if no vaues passed it delivers error
# print(total)

def sum(num1,num2=3):
    if (type(num1) is not int or  type(num2) is not int):
        return
    return num1 + num2

total = sum(2) #since a is not an integer output will be none
print(total)

def multiple_items(*args):
    print(args)
    print(type(args ))

multiple_items("Dave","Mahesh","john","2")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Dave", last="Gray")
