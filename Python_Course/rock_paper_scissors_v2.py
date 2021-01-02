print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("enter Player 1\'s choice: ")
print("***NO CHEATING***\n" * 20)
player2 = input("enter Player 2\'s choice: ")
print("SHOOT!")
if player1 == player2:
    print("DRAW")
elif player1 == 'rock':
    if player2 == 'paper':
        print("player2 wins")
    elif player2 == 'scissors':
        print("player1 wins")
elif player1 == 'paper':
    if player2 == 'rock':
        print("player1 wins")
    elif player2 == 'scissors':
        print("player2 wins")
elif player1 == 'scissors':
    if player2 == 'rock':
        print("player2 wins")
    elif player2 == 'paper':
        print("player1 wins")
else:
    print("something went wrong")