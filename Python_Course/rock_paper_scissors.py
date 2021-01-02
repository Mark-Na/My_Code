print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("enter Player 1\'s choice: ")
i = 0
for i in range(20):
    i+=1
    print("***NO CHEATING***")
player2 = input("enter Player 2\'s choice: ")
print("SHOOT!")
if player1 == 'rock' and player2 == 'scissors':
    print("player1 wins")
elif player1 == 'rock' and player2 == 'paper':
    print("player2 wins")
elif player1 == 'paper' and player2 == 'rock':
    print("player1 wins")
elif player1 == 'paper' and player2 == 'scissors':
    print("player2 wins")
elif player1 == 'scissors' and player2 == 'rock':
    print("player2 wins")
elif player1 == 'scissors' and player2 == 'paper':
    print("player1 wins")
elif player1 == player2:
    print("DRAW")
else:
    print("something went wrong")
