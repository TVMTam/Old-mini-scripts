import time

while True:
    try:
        lim = int(input('Find primes from 1 to '))
        print('\n')
        break
    except ValueError as err:
        print('There\'s an error: ', err)
        print('Please try again')
start = time.time()

numlist = set(x for x in range(2,lim+1)) # Create an set of integers (2,3,..., input)
num2 = set(x*2 for x in range (2, lim+1) if 2*x < lim + 1)
# def CreateList():
#     lis = [x**2 for x in range(lim) if x**2 < lim]
#     return lis
print (numlist - num2)

end = time.time()
print('Time takes:', end - start )
