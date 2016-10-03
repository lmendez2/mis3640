def isPalindrome(string):
    i = 0 #loop starts at the begginning of the string
    x = len(string) - 1 #compares it to the end of the string
    while i<x:
        if string[i] != string[x]:
            return "no, this is not a palindrome"
        i=i+1 #compare the next letter
        x=x-1 #to the next to last letter
    return "yes, this is a palindrome" #and we keep doing so until either the letters dont mathc or do match

inputstr = input('enter a string:') #asking the user to input a string 

print(isPalindrome(inputstr))
