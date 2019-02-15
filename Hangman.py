import time
from random import choice

with open("Users", "r") as file:
    users = file.readlines()
    
with open('Words', 'r') as file:
    words = file.readlines()

name = input("What is your name? ")
if name in users:
    print(f"Welcome back {name}")
else:
    print(f"Hello {name}, Time to play hangman!")
    with open("Users", "a") as file:
        file.write("\n" + name)

time.sleep(1)
print("Start guessing...")
time.sleep(0.5)

def PlayHangman():
    word = choice(words)
    guesses = ''
    turns = 10

    while True:         
        failed = 0
        
        for char in word:      
            if char in guesses:    
                print(char, end = " ")    
            else:
                print("_", end = " ")     
                failed += 1    
        print("")
        if failed == 0:
            print("You won!")
            break              

        guess = input("guess a character:")
        if guess in guesses:
            print("You alreay guessed that!\nGuess something else.")
        elif len(guess) > 1:
            print("Guess ONE character")
        else:
            guesses += guess
            if guess not in word:  
                turns -= 1        
                print("Wrong")    
                if turns == 0:           
                    print("You Lose")
                    print("The word was", word)
                    break
                else:
                    print(f"You have {turns} more failures")  
    answer = input("Do you want to play again? (y/n)")
    if answer.lower() in {'y', 'yes'}:
        PlayHangman()
PlayHangman()
