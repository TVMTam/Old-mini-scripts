'''http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''
def Fibonnaci():
    num = int(input("How many terms? "))
    if num>=2:
        fib=[1,1]
        for i in range (1,num-1):
            fib.append(fib[i-1]+fib[i])
        print (fib)
    elif num == 1:
        fib=[1]
        print(fib)
    else:
        print("Invalid input, please try again")
        Fibonnaci()
Fibonnaci()
