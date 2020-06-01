'''http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
# ASCII table link: see
https://learn.rmotr.com/python/understanding-unicode-in-python/strings-and-unicode/ascii-in-python
'''
import random

low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
# print (low)
# print (up)
# print (numbers)
# print (symbols)
def Get_Input(text="Give integer: "):
    num = int(input(text))
    return num
def Generator():
    PassLen = Get_Input("Give Length: ")
    if PassLen <1 : PassLen = random.randint(8,25)
    Pass = []
    Which =[]
    Password=""
    global low , up , numbers , symbols
    # I want to choose which list of characters
    print("Pass should includes: lowercase(1), uppercase(2), numbers(3), symbols(4)")
    print("Or press 0 to stop")
    while True:
        temp = Get_Input()
        if temp == 1: Which = list(set(Which)|set(low))
        elif temp == 2: Which = list(set(Which)|set(up))
        elif temp == 3: Which = list(set(Which)|set(numbers))
        elif temp == 4: Which = list(set(Which)|set(symbols))
        elif temp == 0 and Which!=[]: break
        else :
            print ('\nNothing was generated.\nGood Bye!')
            quit()

    for i in range(PassLen):
        Pass.append(Which[random.randint(0,len(Which)-1)])
    for i in Pass:
        Password += i
    print ("New Pass:",Password)    
Generator()
