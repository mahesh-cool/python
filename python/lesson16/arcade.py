import sys
from rps import rps
from guess_number import guess_number

def play_game(name = 'Playerone'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcoe back to the Arcade menu.")
        
        playerchoice = input("\n Please choose a game: \n1 = Rock Paper Scissors \n2= Guess My Number \n\n or press \"x\" to exit the Arcade\n\n")
        
        if playerchoice not in ["1","2","x"]:
            print(f"\n{name}, please enter 1, 2, or  x.")
            return play_game(name)
        
        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice =="2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("\n See you next time!\n")
            sys.exit(f"Bye {name}! bye")

if __name__ == "__main__":
    import argparse

    parser = argparse._ArgumentParser(decription = "Provides a personalized game experience.")
    
    parser.add_argument('-n', '--name', metavare = 'name', required = True, help = ' The name of the person playing the name')
    
    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcace! @")

    play_game(args.name)
