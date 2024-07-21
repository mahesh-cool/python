# Dictionaries.py
band = {
    "vocals": "plant",
    "guitar": "Page"
    }

band2 = dict(vocals="Plant", guitar="Page") # dictonary commnad used

print(band)
print(band2)
print(type(band)) #prints type of the band
print(len(band)) # print the length of the file

#Access Items
print(band["vocals"]) # prints value associated to vocals
print(band.get("guitar")) #prints value associated to guitar

# list all keys
print(band.keys())

# list all values
print(band.values())

#list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

#change values
band["vocals"]= "Coverdale"
band.update({"bass":"JPJ"})

print(band)

#Remove items
print(band.pop("bass"))
print(band)

band["drums"]="Bonham"
print(band)

print(band.popitem()) #tuple
print(band)


# De lete and clear items

band["drums"]="Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2


#copy dictionaries

# band2 = band # create a referrence  referring to same dictionaries
# print("Bad Copy")
# print(band2)
# print(band)

# band2["drums"] ="Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Goody copy!")
print(band3)

#Nested Dictionaries

member1 = {
   "name":"plant",
   "instrument": "vocals" 
}
member2 = { 
    "name":"page",
    "instrument": "guitar"
}
band = {
    "member1" : member1,
    "member2" : member2
  }
print(band)
print(band["member1"]["name"])

# Sets

nums ={1,2,3,4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicate allowed
nums =  {1,2,3,2,4}
print(nums)
      
#True is dupe of 1, False is a dupe of zer
nums= {1,True,2,False, 3,4,0} #true is considered as 1 and false is considered as 0
print(nums)

#check if a value is in a set
print(2 in nums)

#But you cannot refer to an element in the set with an index position or a key
#Add an new element to a set
nums.add(8)
print(nums)
 
 #you  can add multiple set to existing dictionaries
morenums = {5,6,7}
nums.update(morenums) # adding morenums data to nums
print(nums)

# you can use update with list, tuples and dictionaries, too
#merge two sets to create a new set
one = {1,2,3,4,5}
two = {5,6,7,8,9}

mynewset = one.union(two)
print(mynewset) # joins two data set one and two

one.intersection_update(two) # compare the common(identical values) data between on one and two
print(one) # print the common data 5 as output

one = {1,2,3,4,5}
two = {5,6,7,8,9}
one.symmetric_difference_update(two) # compare the non identical data from one and two
print(one)