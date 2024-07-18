import sys
import random

def guess_number(name = 'Playerone'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal game_count
        nonlocal player_wins
        
        playerchoice = input(f"\n{name}, guess which number I'm thinking of ...1, 2,3 \n")
        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number()
        
        computerchoice = random.choice("123")

        print(f"\n{name} , you choose{playerchoice}.")
        print(f"I was thinking about the number{computerchoice}. \n")

        player = int(playerchoice)

        computer = int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins +=1
                return f" celebrate {name}, you win!"
            else:
                return f"Sorry,{name}. Better luck next time. sad"
        
        game_result = decide_winner(player, computer)
        
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\n Your Winning percentage : {player_wins/game_count:.2%}")
        
        print(f"\n play again,{name} ?")

        while True:
            playagain = input("\n Y for yes or \n Q to quit \n")
            if playagain.lower() not in ["y","q"]:
                continue
            else :
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\n celebrate celebrate")
            print("Thank you for playing!\n")
            if __name__== "__main__":
                sys.exit(f"Bye{name}! bye")
            else :
                return
                
    return play_guess_number

if __name__== "__main__":
    import argparse

    parser = argparse.ArgumentParser( decription = " Provices a personalized game experience.")

    parser.add_argument('-n', '--name', metavar ='name',required=True, help= 'The name of the person playing the game.')
    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()



        