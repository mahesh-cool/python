name = "mahesh" #global variable for name
count = 1  #global variable fro count
# greeting("John")

def another():
    color = "blue"
    global count # defining global variable inside the function
    count += 1
    # count = 2 local definition inside the function
    print(count)

    def greeting(name):# definition for function
        nonlocal color # defining local colour for function
        color = "red" #used for greeting function only
        print(color) # print local function colour
        print(name)#print global name
        print(count) # print another function result adding +1
    # print(firstname)
    greeting("Dave")
print(count)
another()

# def san():
#      another("mahsh")
#      print(name)
    

# san("mahesh")