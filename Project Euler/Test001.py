import time

start = time.time()
primes = [1,2]

lis = list(range(3,100))

for i in lis:
    primes.append(i)
    if i % 2 == 0:
        lis.pop(lis.index(i))

primes = primes+lis

end = time.time()
print('Time takes:', end - start )
