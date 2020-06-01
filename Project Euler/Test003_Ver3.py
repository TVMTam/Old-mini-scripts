"""
Find prime under 1000 using list
"""
import time
start = time.time()

all_num_list =[i*2+1 for i in range(2,50000)]
# print (all_num_list)
prime_list = [1]

while len(all_num_list) > 1:
    holder = all_num_list[0]
    remover =[]
    prime_list.append(holder)
    print ("Add {0} into prime_list".format(holder))

    # print ("{0} is now removed from all_num_list".format(holder))
    all_num_list = all_num_list[1:]
    # print(all_num_list)

    remover = [i for i in all_num_list if i % holder == 0]
    # print("These number will be removed")
    # print(remover)


    a = set(all_num_list)
    b = set(remover)
    c = a-b
    # print ("POPIPO")
    # print (c)
    all_num_list = list(c)
    all_num_list.sort()
    # print (all_num_list)

print ("\nHere's the result:")
print (prime_list)

end = time.time()
print("It took me {}s to do this.".format(end-start))

f = open("Output001.txt","w+")
f.write(str(prime_list))
f.close()
