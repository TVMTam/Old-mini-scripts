"""http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
age = 2018 + (100 - age)

statement = 'The year '+ name +' turns 100 is: ' + str(age)
print (statement)
num = int(input("Enter another number: "))
print (statement*num)
print ((statement+'\n')*num)
