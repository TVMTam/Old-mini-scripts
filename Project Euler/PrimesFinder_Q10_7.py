'Find n first primes'
import time
# prompt input from user
while True:
    try:
        lim = int(input('Find primes from 1 to '))
        print('\n')
        break
    except ValueError as err:
        print('There\'s an error: ', err)
        print('Please try again')

primes = [1] # This is the list of primes
start = time.time()

# Prime cheking algorithm
for num in range(2, lim+1):
    count = 0
    # print('Prime checking number:', num)
    for ind in range(1, num+1):
        if num % ind == 0:
            count += 1
            # print (num,'can be divided with', ind)
            if count > 2: break
    # print (count)
    if count > 2:
        # print(num,'is skipped')
        continue
    if count == 2:
        primes.append(num)
        # print(num,'is added to primes list')

end = time.time()
print ('list of primes:', primes)
print ('number of primes:',len(primes))
print ('time takes:',end - start)
