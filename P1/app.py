# > This is Small Game  Using Random Method
# > ['Stone', 'Paper', 'Sizer'] && ['Snake', 'Water', 'Gun']

import random as rd

options = ['stone','paper','sizer']

def Computer():
    computer_opt = rd.choice([1,2,3])
    return computer_opt

def Player(options):
    player_inp = input("Enter Your Choice > ").lower()
    player_opt = 1 if player_inp == options[0] else 2 if player_inp == options[1] else 3 if player_inp == options[2] else 4 # one liner if-else
    return player_opt

def Main(computer, player):
    if (computer == player):
        return("It's a tie!")
    elif ((computer == 1) and (player == 2))or((computer == 2) and (player == 3))or((computer == 3) and (player == 1)):
        return("You win!")
    elif ((computer == 3) and (player == 2))or((computer == 2) and (player == 1))or((computer == 1) and (player == 3)):
        return("You Lose!")
    else:
        return("please select given options ...")

player = Player(options)
computer = Computer()

output = Main(computer, player)
print(output)