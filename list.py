list_1= [2,3,4,5] # regular list 
AFC_east=[ 'cat', 'dog','duck',' bunny'] #regular list 

a_nested_list = ['spam',2.0,5, [10,20 ]] #nested list with four elements one being another list
print(AFC_east)

AFC_east[3]='chicken' #list indices work same as stron cat=0 dog=1 and so on so bunny is now chicke
print(AFC_east)

print(AFC_east[0:2]) #start at 0 and stop at 2 not inclusive
print(AFC_east[2:4]) #start at 2 inclusive stop before end 
print(AFC_east[-2:]) #same way

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print(L[0]) #calls the first element within the list
print(L[0][0])#first element within the first element
print(L[2][2]) #lisa
print(L[1][2][1]) #on rail


numbers = [2, 0, 1, 6, 9]
for i in range (len(numbers)):
    numbers[i] = numbers[i] *2

print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list)) #elements in the list: four 


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b #this adds the lists elemnts together not the numbers
print(c)


m=[]
m.append(a)
m.append(b)
print(m)

print([0]*4)
print(['Tom Brady', 'Bill Belichick']*3)

t = ['a', 'b', 'c', 'd', 'e', 'f']

print(t[1:3])
#bc
print(t[:4])
#abcd
print(t[3:])
#def

t[1:3] = ['x', 'y'] #replaces whats in the list in those numbers
print(t)

t = ['a','b','c']
t.append('d')
print(t)

t.extend(L) #extends the list to add another list
print(t)

t.insert(0,L) #in that space an item is inserted
print(t)