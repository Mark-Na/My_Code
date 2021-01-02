from random import randint
print("...rock...")
print("...paper...")
print("...scissors...")
flag = True
p1 = 0
comp = 0
while (flag == True):
    player = input("enter your choice: ").lower()
    if player == 'exit':
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'
    print(f"Computer plays {computer}")
    print("SHOOT!")
    if player == computer:
        print("DRAW")
        print(f"Player {p1} and computer {comp}")
    elif player == 'rock':
        if computer == 'paper':
            print("computer wins")
            comp+=1
            print(f"Player {p1} and computer {comp}")
        else:
            print("player wins")
            p1+=1
            print(f"Player {p1} and computer {comp}")
    elif player == 'paper':
        if computer == 'rock':
            print("player wins")
            p1+=1
            print(f"Player {p1} and computer {comp}")
        else:
            print("computer wins")
            comp+=1
            print(f"Player {p1} and computer {comp}")
    elif player == 'scissors':
        if computer == 'rock':
            print("computer wins")
            comp+=1
            print(f"Player {p1} and computer {comp}")
        else:
            print("player wins")
            p1+=1
            print(f"Player {p1} and computer {comp}")
    else:
        print("something went wrong")
