'''http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
    In a previous exercise(Ex_009), we’ve written a program that “knows” a number and asks a user to guess it.

    This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

    At the end of this exchange, your program should print out how many guesses it took to get your number.

    As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)'''
import random

print("Think about a number between 0 and 100. I will guess it.")
def MyGuess(help_text = "Is your number "):
    guess = random.randint(45,55)
    guess_list=[i for i in range(101)]
    count = 0
    def take_input():
        while True:
            try:
                user = int(input("Too low(1), Too high(2), Yes(3)\n"))
                return user
            except:
                print("Invalid input. please try again")
                continue


    while True:
        print (help_text+'{0}?'.format(guess))
        user = take_input()
        
        if user == 3:
            print("I made it after {0} tries.".format(count))
            print("Game over. Have a nice day!")
            break
        elif user == 2:
            print ("I'll find a lower number next time\n")
            guess_list = guess_list[:guess_list.index(guess)]
            guess = random.choice(guess_list)
            # print ("my guess are from", guess_list)
        elif user == 1:
            print ("I'll find a higher number next time\n")
            guess_list = guess_list[guess_list.index(guess):]
            guess  = random.choice(guess_list)
            # print ("my guess are from", guess_list)
        count+=1
MyGuess()
