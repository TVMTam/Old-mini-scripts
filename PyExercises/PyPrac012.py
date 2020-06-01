'''http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''
import random
a = random.sample(range(20),5)
def EndCut():
    print(a)
    print (a[0])
    print (a[-1])
EndCut()
