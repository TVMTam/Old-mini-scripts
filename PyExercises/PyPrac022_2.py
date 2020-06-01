'''http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
Extra:
Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file("Ex_22_Training_01.txt"), and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3 I talked a little bit about it in this post.'''
import re
File = "Ex_22_Training_01.txt"
with open(File) as open_file:
    pattern = ".+/"
    word_dict=dict()
    for line in open_file:
        line = line[3:].strip() #remove the first "/./" character
        line = re.findall(pattern,line)[0][:-1]
                # take the list of match, take first ele with the last char (/) removed
        if line not in word_dict:
            word_dict[line]=1
        else: word_dict[line]+=1
    # print(word_dict)
    for k,v in word_dict.items():
        print ("there are {0} items in {{{1}}}".format(v,k))
