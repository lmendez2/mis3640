#fin = open('words.txt')
#line = repr(fin.readline())
#https://docs.python.org/3/library/functions.html#repr

#fin = open('words.txt')
#for line in fin:
 #   word = line.strip()
   # print(word)


def read_long_words():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) >20: #length is greater than 20
            print(word)

read_long_words()


   
    #prints only the words with more than 20 characters
    
   


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    #look for letter in word
    """
    for letter in word: #looking for letters in words
        if letter == 'e': #only e 
            return False # if not found continue #if found return false right away 
    return True #return true 

print(has_no_e('babson'))
print(has_no_e('college'))

def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in word:
        if letter in forbidden: #searching for forbidden letters in words to avoid 
            return False #if found return false
    return True #if not found return true 
    
print(avoids('babson', 'ab')) #false 
print(avoids('college','ab')) #true and true


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list. 
    """
    for letter in word: #opposite of the previous, now we are search for specifics
        if letter not in available:
            return False #can't find the strings needed
    return True #found the strings needed

print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('College', 'aBbsonxyz'))
    


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    return uses_only(required,word) # going back to previous function 

print(uses_all('Babson', 'abs')) #previous function will return true because abs is requied
print(uses_all('college', 'abs')) #false, abs is not present 



def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = word[0] #starts at the first letter of the word, then the next =0 
    for letter in word:
        if letter < before:
            return False 
        before = letter #can work if the letter is the same as before or True
    return True

print(is_abecedarian('abs')) #should be true a<b<s
print(is_abecedarian('college')) #should be false o is greater than l 


def factorial (n): # i included this just to understand recursive a little better before tackling the next exercise 
    if n == 0:
        return 1 #special case of finding the factorial zero 
    else:
        return n * factorial(n-1) # n* n!

print(factorial(5))
print(factorial(0))

def is_abecedarian(word): #using recursion 
    if len(word) <= 1 : #a is still a word and would still hold true technically
        return True 
    if word[0] > word [1]: #compare letter before with letter 0v1
        return False
    return is_abecedarian(word[1:]) #we go back to the previous 

print(is_abecedarian('abs')) #should still be true 
print(is_abecedarian('college')) #should still be false

def is_abecedarian(word): #using loop 
    i = 0 #where the loop starts 
    while i < len(word)-1: #because the length is len(word)-1
        if word [i+1] < word[i]: #compares i vs i+1 or current and next
            return False
        i = i+1
    return True 

print(is_abecedarian('abs')) #should still be true 
print(is_abecedarian('college'))