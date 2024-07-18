import math #Import the math module
#from match import pi #  on imports the pi from math module
import sys # import sys module
import random as rdm # usign random as rdm in program

import  chennai # customized module 
print(math.pi) # print the value of pi in output

from rps7 import rock_paper_scissors
# print(dir(rdm)) print the module rdm in unformated
# for item in dir(rdm): 
#     print(item)
# print the options in random(rdm) in formated way

print(chennai.capital)# printing customized module data
chennai.randomfacts()# printing random facts from module

print(__name__)# name module from chennai file
print(chennai.__name__)

rock_paper_scissors()
