##import necessary library
import random

##set variables
play = "yes"

##guess loop

while play == "yes":
    guess, guess_limit, secret_number = None, 0, random.randint(1,10)
    print(secret_number)
    while guess != secret_number and guess_limit < 5:

        while guess_limit < 5:
            guess_limit += 1
            guess = int(input("Enter your number guess: \n"))
            if guess == secret_number:
                print("You've guessed it!")
                break
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
    
        if guess_limit >= 5:
            print("You've reached your attempt limit.")
          
    play = input("Do you want to play again?")