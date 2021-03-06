"""http://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.

    In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

    Draw the Tic Tac Toe game board
    Checking whether a game board has a winner
    Handle a player move from user input
    The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend. There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

    Here are a few things to keep in mind:

    You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
    If there are no more moves left, don’t ask for the next player’s move!
    As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.
    """

# def Board(help_text="Give number: "):
#     user = 3
#     def Horizontal():
#         cell = " ---"
#         print(cell*user)
#
#     def Vertical():
#         cell = "|   "
#         print ((cell*(user+1)).rstrip())
#
#     for k in range(user):
#         Horizontal()
#         Vertical()
#     Horizontal()
# Board()
Board = """ --- --- ---
| {0} | {1} | {2} |
 --- --- ---
| {3} | {4} | {5} |
 --- --- ---
| {6} | {7} | {8} |
 --- --- ---
"""
Position = [" "," "," "," "," "," "," "," "," "]
print (Board.format(*Position))
print(type(Board))
