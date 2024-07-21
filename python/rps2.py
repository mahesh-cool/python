# value = input('please enter a value: \n')
# print(value)
import sys
import random
from enum import Enum
 

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    
    playerchoice = input("\n Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)
    # if 1 > 2 :
    #     print('do something')

    if player < 1 or player > 3 :
        sys.exit("You must enter1, 2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    # without using enum 
    # print("")
    # print("your choose "+ playerchoice + ".")
    # print("python chose " + computerchoice + ".")
    # print("")

    #with using Enum
    
    print("\n your choose "+ str(RPS(player)).replace('RPS.','') + ".")
    print("python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")
    

    if player == 1 and computer == 3:
        print("celebrate you win!")
    elif player == 2 and computer == 1:
        print("You win")
    elif player == 3 and computer == 2 :
        print("you win!")
    elif player == computer :
        print("Tie game!")
    else:
        print("Python Wins!")
    
    playagain = input("\n Play again? \nY for yes or \n Q t quit \n\n")
    
    if playagain.lower() == "y":
        continue
    else:
        print("\n celebrate")
        print("Thank for playing!\n" )
        playagain =False
sys.exit("Bye! ")
