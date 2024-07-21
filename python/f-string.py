person = "Dave"
coins = 3

print ("\n" + person + " has " + str(coins) + " coins left.") # print
#concatenating commands for the print
message = "\n%s has %s coins left." %(person,coins) # older way of concatenating words
print(message)


message = "\n{} has {} coins left." .format(person,coins) # format method of printing texts
print(message)


message = "\n{1} has {0} coins left." .format(person,coins) 
# numbers inside curly bracket defines the position of the statuesme
#out put will be 3 has dave coins left
print(message)

message = "\n{1} has {0} coins left." .format(coins,person)
#replaing coins and person give s the correct format of data
print(message)

message = "\n{person} has {coins} coins left." .format(coins=coins,person=person)
#replaing coins and person give s the correct format of data
print(message)


# message = "\n{person} has {coins} coins left." .format(coins,person)
# # #replaing coins and person give s the correct format of data
# print(message)


player = {'person': 'Dave', 'coins': 3}# dictionary format file
message = "\n{person} has {coins} coins left." .format(**player)
#formating with dictionary
print(message)
###################################
#F-String! this is the way.
message = f"\n{person} has {6*2} coins left." #using fstring functions
# we can define individual function inside the curly functions
print (message)

message = f"\n{person.lower()} has {6*2} coins left." #using lower() print strign in lower case
# we can define individual function inside the curly functions
print (message)


message = f"\n{player['person'].lower()} has {6*2} coins left." #using lower() print strign in lower case
# we can define individual function inside the curly functions
print (message)

######################
#we can pass formatting options

num =10
print(f"\n2.25 times {num} is {2.25*num:.2f}")
#2f define number of decimal in above line
for num in range(1,11):
    print(f" \n 2.25 times {num} is {2.25 * num:.2f}")
# we are using range from 1 to 11 to iterate the value 

for num in range(1,11):
    print(f" \n {num} divided by 4.52 is {num /4.52:.2%}")