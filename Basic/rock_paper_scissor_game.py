# The Program
import random

first_player = input(str("Please state your name:- "))

second_player = input(str("Please state your name:- "))

p1 = (0)
p2 = (0)

rps = ["Rock","Paper","Scissor"]

for i in range(5):
    
    player1 = random.choice(rps)
    
    player2 = random.choice(rps)
    
    print(f'\n{first_player} your hand is {player1}\n{second_player} your hand is {player2}\n')

    if player1 == "Rock" and player2 == "Paper":
        p2 = p2 + 1
    
    elif player2 == "Rock" and player1 == "Paper":
        p1 = p1 + 1

    elif player2 == "Scissor" and player1 == "Paper":
        p2 = p2 + 1

    elif player1 == "Scissor" and player2 == "Paper":
        p1 = p1 + 1

    elif player1 == "Rock" and player2 == "Scissor":
        p1 = p1 + 1

    elif player2 == "Rock" and player1 == "Scissor":
        p2 = p2 + 1
    
    elif player1 == player2:
        print(f'{first_player} same hand as {second_player}\n')
    
    else:
        print("Error 404")
        
    print(f'{first_player} has {p1} and {second_player} has {p2}\n')


if p2 > p1:
    print(f'{second_player} wins with {p2}')
    print(f'Thanks for playing {second_player}')
    print(f'Good luck next time {first_player}')

elif  p1 > p2:
    print(f'{first_player} wins with {p1}')
    print(f'Thanks for playing {first_player}')
    print(f'Good luck next time {second_player}')

elif p1 == p2:
    print("This is a tie")

else:
    print("Error 505")
