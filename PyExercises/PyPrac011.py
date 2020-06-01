'''http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
'''
def CheckPrime(help_text="Please enter a number: "):
    num = int(input(help_text))
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            print(num,'can be divided by',i)
            count+=1
            if count >2:
                print(num,'is not prime')
                break
    if count==2: print(num,'is prime')

CheckPrime()
