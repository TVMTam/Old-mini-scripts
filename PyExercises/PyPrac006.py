'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)'''

string = input("Please type a string to check for palindromity: ").lower()
reverse = string[::-1]
if string == reverse:
    print(string, 'is a palindrome')
else:
    print(string, 'is not a palindrome')
