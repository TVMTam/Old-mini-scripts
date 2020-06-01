"""By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)"""

# I'm trying to convert each row to a list of numbers
pyramid ="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
newlist = pyramid.split("\n")
# print(newlist)

#now I get a list of each line
#convert each space into a list of numbers
temp = 0
for line in newlist:
    newlist[temp] = line.split(" ")
    temp1 = 0
    for element in newlist[temp]:
        newlist[temp][temp1] = int(newlist[temp][temp1])
        temp1+=1
    temp+=1
# print (newlist)
for i in newlist:
    print (i)

#Finding a path:
line = 0
position = 0
begin = newlist[line][position]
possible_1 = position
possible_2 = position + 1
path = [begin]

print ("start!")
for each_line in newlist[1:]:
    # print ("checking",each_line)
    count = 0
    for num in each_line:
        if count == position:
            next = each_line[position+1]
            print ("Underneath {2} is {0} and {1}".format(num,next,begin))
            if num > next:
                path.append(num)
                # print ("added",num)
                begin = num
                position = count
                break
            else:
                path.append(next)
                # print("added",next)
                begin = next
                position = count +1
                break
        count +=1

print (path)

#Calculate Sum
sum = 0
for ele in path:
    sum+=ele
print (sum)

#The top down approach wont neccessary give the largest total since some of the big number can be missed if the numbers above them were small
# https://stackoverflow.com/questions/8002252/euler-project-18-approach
