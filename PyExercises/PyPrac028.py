"""Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!"""

def Compare(help_text="Give {0} number: "):
    command = ["First","Second","Third"]
    numlist = [float(input(help_text.format(i))) for i in command]
    print (numlist)
    largest = 0
    for k in numlist:
        if k > largest: largest = k
    print ("The largest number is", largest)        
Compare()
