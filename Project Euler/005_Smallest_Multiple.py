'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
numlist = []
mu3 = []
for i in range(2,21):
    numlist.append(i)
    if 2*i <= 100:
        mu3.append(2*i)
    if 3*i <=100:
        mu3.append(3*i)
    if 5*i <=100:
        mu3.append(5*i)
    if 7*i <=100:
        mu3.append(7*i)
    if 11*i <=100:
        mu3.append(11*i)
    if 13*i <=100:
        mu3.append(13*i)
    if 17*i <=100:
        mu3.append(17*i)
    if 19*i <=100:
        mu3.append(19*i)
MU3 = set(mu3)
MU = set(numlist)
prime = MU-MU3
print (prime)
numlist = []
for k in range(1,21):
    
