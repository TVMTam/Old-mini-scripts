'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143 ?'''

#a = 600851475143
numlist = []
mu2 = []
mu3 = []
for i in range(2,101):
    numlist.append(i)
    if 2*i <= 100:
        mu2.append(2*i)
    if 3*i <=100:
        mu3.append(3*i)
    if 5*i <=100:
        mu3.append(5*i)
    if 7*i <=100:
        mu3.append(7*i)
print (mu2)
MU2 = set(mu2)
MU3 = set(mu3)
MU = set(numlist)
print (MU-MU2-MU3)
