users = ['Dave','John','Sara'] # list of users

data = ['Dave',42,True] #data list

emptylist = [] # empty list no users

print("Dave" in emptylist) # validate dave user in empty list
#print("Dave" in data) # validate dave in data list if available it print dave and true

print(users[0])  #  0 represent first value in the list
# print(users[-1]) # -1 represencts the last value in the list
print(users[-2]) # -2 represents value prior to last 

print(users.index('Sara')) # position of data  it show 2

print(len(data)) # print the data length

users.append('Elsa') # one of the method to add user to list
print(users)

users +=['Jason'] # second methond to add data to list
print(users)

# users += 'Jason' # print data in each letter if not place in brackets

users.extend(['Robert','Jimmy']) 
print(users)

# users.extend(data) # add the extended new user to data list
# print(users)

users.insert(0,'Bob') # inster bob to the list
print(users)

users[2:2] = ['Eddie', 'Alex']# add users to the second position of the list
print( users)

users[1:3] = ['Robert','JPJ']# replace the users in first and 3rd position of the list
print(users)

users.remove('Bob') # remove the user bob from list
print(users)

print(users.pop())# remove the last user from the list
print(users)

del users[0]# remove the first user from the list
print(users)

# del data   # command to delete data
data.clear() # clear data in the list
print(data)

users[1:2] =  ['dave'] # insert dave to the list
users.sort() # sor the users in the alphabets
print(users)


users[1:2] =  ['dave'] # insert dave to the list
users.sort(key=str.lower) # sor the users in the alphabets
print(users)

nums = [56,5,78,96,2]
nums.reverse()
print(nums)

# nums.sort(reverse = True)
# print(nums)

print(sorted(nums,reverse = True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,'Neil',True])
print(mylist)

#Tuples

mytuple = tuple(('Dave',42,True))

anothertuple = (1,4,2,82,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two,  hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
