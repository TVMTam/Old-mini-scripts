'''http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
    This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2(Ex_26), Part 3(Ex_27), and Part 4(Ex_29).

    Time for some fake graphics! Let’s say we want to draw game boards that look like this:

     --- --- ---
    |   |   |   |
     --- --- ---
    |   |   |   |
     --- --- ---
    |   |   |   |
     --- --- ---
    This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

    Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

    The main topic of this exercise is functions. They are tricky, and deserve lots of practice and thought. '''

def Board(help_text="Give number: "):
    user = int(input(help_text))
    def Horizontal():
        cell = " ---"
        print(cell*user)

    def Vertical():
        cell = "|   "
        print (cell*(user+1))

    for k in range(user):
        Horizontal()
        Vertical()
    Horizontal()
Board()
