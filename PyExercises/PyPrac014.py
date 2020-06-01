'''http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:
1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
AAA = [1,2,3,4,5,6,7,3,4,5,7,8,9]
list2 = [4,5,6,7,9,1,2,4,5]

def F1():
    global AAA # Without this, there's an error:
    # UnboundLocalError: local variable 'AAA' referenced before assignment
    # Function only assign local var and search for local var only. If I want to assign a variable outside function: use 'global'. This issue can also be solved by moving AAA inside F1.
    AAA = list(set(AAA))
    print(AAA)
def F2():
    temp=[]
    for i in AAA:
        if i not in temp:
            temp.append(i)
    print (AAA)
F1()
F2()
