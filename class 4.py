def print_lyrics(): #define functions
    print("hey jude. Dont make it bad")
    print("take a sad song and make it better.")



print(type(print_lyrics)) #prints what print_lyrics is which is function 

print_lyrics() #prints the lyrics

def repeat_lyrics():
    print_lyrics()
    print("na na na na na na")
    print_lyrics()

repeat_lyrics() #prints the repeated lyrics

def print_twice(l):
    print(l)
    print(l)

print_twice('babson')

my_name = 'lauren'
print_twice(my_name)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1= 'bing tiddle'
line2= 'tiddle bang'
cat_twice(line1, line2)


def give_me_a_break():
    str1 = 'break'
    print('another break')
    return str1
    
new_str = give_me_a_break()

print(new_str)
#give_me_a_break()

#print(give_me_a_break())


#def a_new_function_demo():
  #  s = 0 
   # for x in 'dog':
    #    print(x)
#print(ord(x))
      #  s = s + ord(s)
#return s


#print(a_new_function_demo())


input()