"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?"""

power = 1000
base = 2

result = str(base**power)
print(result)
print(type(result))

sum = 0
for letter in result:
	sum += int(letter)
print (sum)
