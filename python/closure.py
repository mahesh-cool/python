#closure is a function having access to the scope of its parent
#fuction after the parent fuctin has returend


# def parent_function(person) incase not defining global variable coins 
def parent_function(person, coins):
    # coins = 3  # global variable to 
    def play_game():
        nonlocal coins
        coins -=1
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " +str (coins) + " coins left.")
        else:
            print("\n" + person  + " is out of coins. ")

    return play_game

tommy = parent_function("Tommy" , 5)# if global variable is not defined we can define funciton value directly
jenny = parent_function("Jenny" , 8) 

tommy()
tommy()
jenny()
tommy()