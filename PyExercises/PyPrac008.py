'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)'''
while True:
    print("Rock(1), Paper(2) or Scissors(3)?")
    P1 = int(input('Player 1\'s hand: '))
    P2 = int(input('Player 2\'s hand: '))
    if P1 == P2:
        print("Draw!")
    else:
        if P1 == 1:
            if P2 == 2:
                PW = 2
            else: PW = 1
        elif P1 == 2:
            if P2 ==1:
                PW = 1
            else: PW = 2
        elif P1 ==3:
            if P2 ==1:
                PW = 2
            else: PW =1
        print('Player',PW,'wins')
    con = input ("Continue? (Y/N) ").lower()
    if con == 'n': quit()
