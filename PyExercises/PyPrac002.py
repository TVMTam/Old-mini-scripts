'''http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

1.If the number is a multiple of 4, print out a different message.
2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.'''
num = int(input('Enter a number: '))
if num%4==0: print("BINGO!")
elif num%2==0:
    print (num,"is an EVEN number")
else:
    print (num,"is an ODD number")
num = int(input('Enter a number to check: '))
check =  int(input('Enter a number to divide by: '))
if num%check ==0 :
    print(num,'can be divided evenly into', check)
else:
    print (num, 'cannot divided by', check)
