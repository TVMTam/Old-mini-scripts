'''http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.(Hint: Remember list comprehensions from Exercise 7).

Extra:

Randomly generate two lists to test this'''
import random
# num_list = int(input("Number of lists: "))
list_len = random.randint(3,10)
temp1 = [random.randint(3,20) for i in range(list_len)]
temp1.sort()
list_len = random.randint(3,10)
temp2 = [random.randint(3,20) for i in range(list_len)]
temp2.sort()
print (temp1)
print (temp2)
lis=[]
for i in temp1:
	if i in temp2 and i not in lis:
		lis.append(i)
lis.sort() #unnecessary since the lists above is sorted already

print (lis)
