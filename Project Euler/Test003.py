"""Find prime under 1000 using list
"""

all_num_list =[i for i in range(2,100)]
print (all_num_list)
prime_list = [1]

for NUM in all_num_list:
    prime_list.append(NUM)
    print ("Add {0} into prime_list".format(NUM))
    for ilter in all_num_list:
        if ilter % NUM == 0:
            all_num_list.remove(ilter)
            print ("Remove {0} which has {1} as factor".format(ilter,NUM))
    print (all_num_list)
