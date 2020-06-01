'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?'''
import re

with open("Names.txt") as hdl:
    text = hdl.read()
    # print (text)

#Create name_list
temp = 0
name_list = text.split(",")
for name in name_list:
    name_list[temp] = name[1:-1] # Remove '' signs
    name_list[temp] = name_list[temp].lower() # Convert to lowercase to simplify calculation
    temp += 1
# print (name_list)

#sorting names into alphabetical order
name_list.sort()

# working out the alphabetical value for each name
tot_temp = 0 # use to count total
tot = 0
position = 1
for name in name_list:
    print ("Analysing",name,"at position",position)
    for character in name:
        temp = ord(character)-ord("a")+1
        # print (character, temp)
        tot_temp += temp
    tot += tot_temp * position # accrual tot
    tot_temp = 0 # reset tot_temp for the next name
    position += 1 # update position of next name
print ("The total of all alphabetical value is",tot)
