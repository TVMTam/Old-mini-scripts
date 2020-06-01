"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""
import random

while True:
    num = random.randint(1,9)
    count = 0

    while True:
        u = input("Guess a number between 1 and 9: ")
        if u == 'exit':quit()
        else:
            u = int(u)
            count+=1
        if u<num:
            print('Too low\n')
        elif u>num:
            print('Too high\n')
        else:
            print ("Correct!\n")
            break
    print("Success after {} trials".format(count))
    break
