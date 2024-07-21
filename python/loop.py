#using break function
# value = 1
# while value < 10: # condition to maximum value running loop till condition satisfied
#     print(value)
#     if value ==5: #sub condition to stop loop till this condition satisfied
#         break
#     value +=1

#using continue command
#     while value <=10:
#         value +=1
#         if value ==5:
#             continue
#         print(value)
#     else:
#         print("Value is now Equal to " +str(value))# defining string value inside the bracket

#For loop
names= ["Dave","Sara","John"]
# for x in names:
#     print(x)
    
# for x in "Mississippi":
#     print(x)
# for x in names:
#     if x =="Sara":# from names it iterates till sara is identified
#         break# it brakes the loop once condition above is satisfied
#     print(x)

# for x in names:
#     if  x =="Sara":
#         continue # this command contiunes the iteration after x is resolved
#     print(x)

# for x in range(4): # prints value 0 to 3  and 4 is not iterated
#     print(x)

# for x in range(2,5):# print value from 2 to 4 and not 5 
#     print(x)

for x in range(0,100 , 5):# first digit is start of the range and second is ending digit and 3rd value is interval between the values
        print(x)
else:
        print("Glad thats\'s over") # \ is used for space between the words

names = ["Dave","Sara","John"]
actions = ["Codes","Eats","Sleeps"]
# for name in names:
#         for action in actions:
#                 print(name+" "+action+".") # iterated names and actions for each words

for  action in actions:
        for name in names:
                print(action + " " + name +".") #iterated  action with names
                







