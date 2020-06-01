"""http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. "Ex_23_primenumbers.txt" file has a list of all prime numbers under 1000, and the "Ex_23_happynumbers.txt" file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)"""
with open("Ex_23_primenumbers.txt") as op_prime:
    prime = op_prime.read().strip()
with open("Ex_23_happynumbers.txt") as op_happy:
    happy = op_happy.read().strip()
prime_list = prime.split("\n")
happy_list = happy.split("\n")
    # create list of strings of prime/happy
# print (prime_list)
# print (happy_list)
a = set(prime_list)&set(happy_list)  #find overlap using set operation
a = list(int(i) for i in a) # convert to set to list, string to integer
a.sort()

print (a)
