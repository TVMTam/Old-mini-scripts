'''http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you("Ex_22_nameslist.txt"), if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file("Ex_22_Training_01.txt"), and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.'''

# User = input("Which file to read? ")
# if len(User)==1: User = "Ex_22_nameslist"
# else: User = "Ex_22_Training_01"
File = "Ex_22_nameslist.txt"
with open(File) as OpF:
    name_list = {}
    for line in OpF:
        name = line.strip()
        if name not in name_list:
            name_list[name]=1
        else:
            name_list[name]+=1
    print(name_list)
    for k,v in name_list.items():
        print(k,v)
