"""The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

NaNum = input('Length of natural numbers:')
NaNum = int(NaNum)
S1 = 0
S2 = 0

for ill1 in range(0,(NaNum+1)):
    S1 = S1 + ill1**2
print ('The sum of the squares of the first', NaNum,'natural numbers is:',S1)

for ill2 in range(0,(NaNum+1)):
    S2 = S2 + ill2
S2 = S2 ** 2
print('The square of the sum of the first', NaNum, 'natural numbers is:',S2)

calc = S2 - S1
print('Hence the difference between the sum of the squares of the first', NaNum, 'natural numbers and the square of the sum is:')
print(S2,'-',S1,'=',calc)
