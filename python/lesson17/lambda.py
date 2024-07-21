squared = lambda num:  num * num 
# lambda num : num parameters
print(squared(2))

addTwo = lambda num : num +2 

print(addTwo(12))

# sum = lambda a , b : a + b

# print(sum(2,56))

##############################

#lambda

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

#################################################
#map

numbers = [3,4,6,8,9,89,56]

squared_nums = map(lambda num : num * num , numbers)

print(list(squared_nums))


##########################################
#filters



odd_nums = filter(lambda num : num %2 != 0, numbers)
# condition to print number is odd 
print(list(odd_nums))

even_nums = filter(lambda num : num %2 == 0, numbers)
# condition to identify value is even
print(list(even_nums))


from functools import reduce

# lambda acc, curr: acc + curr

numbers = [1,2,3,4,5,1 ]
total = reduce(lambda acc, curr: acc + curr, numbers,15)

print(total)

print(sum(numbers,45))

lambda acc, curr : acc + len(curr)

names = ['Dave Gray', 'Sara ITo', 'John Jacob Jingle', 'Jingleeheimerschmidst']
char_count = reduce(lambda acc, curr: acc +len (curr), names,0)

print(char_count)