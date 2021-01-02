import random
number = random.randint(1,10)
while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess == number:
        print("You guessed it! You won!")
        answer = input("Do you want to play again? (y/n) ")
        if answer == 'y':
            number = random.randint(1,10)            
        else:
            print("Thank you for playing!")
            break
            
    elif guess < number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

