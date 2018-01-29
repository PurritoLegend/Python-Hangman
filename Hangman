import time
from random import choice

file = open("Users", "r")
users = file.read().splitlines()

name = input("What is your name? ")
if name in users:
    print("Welcome back", name)
else:
    print("Hello " + name, ", Time to play hangman!", sep = "")
    filea = open("Users", "a")
    filea.write("\n" + name)
    filea.close()
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)

def PlayHangman():
    wordFile = open('Words', 'r')
    words = wordFile.read().splitlines()

    word = choice(words)
    guesses = ''
    turns = 10
    file = open("Users", "r")

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
            print("You won")
            break              

        guess = input("guess a character:")
        if guess in guesses:
            print("You alreay guessed that \n Guess something else")
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
                    print("You have", + turns, 'more failures')  
    answer = input("Do you want to play again?(y/n)")
    if answer == "y" or answer == "Y" or answer == "yes":
        PlayHangman()
PlayHangman()
        

