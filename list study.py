[10, 20, 30, 40]
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
a = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
print(a, numbers, empty)
a[3] = 'New York Giants'
print(a)
a = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
print('a Bills' in a)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

for pet in a:
    print(pet)

    numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)): #for every iterationof numbers 
    numbers[i] = numbers[i] * 2 #new numbers =*2
    
print(numbers)

my_list = ['spam', 1, 2, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print([0] * 4)


print(['Tom Brady', 'Bill Belichick']*3)


t = ['a', 'b', 'c', 'd', 'e', 'f']

t[1:3] = ['x', 'y']
print(t)

t.insert(1,'k')
print(t)
print(t.index('a'))

b = [1 , 5 , 2, 9]
b.sort()
print(b)
 

b.pop(0)
print(b)


t = ['a', 'b', 'c', 'd', 'e', 'f']
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print(capitalize_all('cat'))

t = [1, 2, 3]
print(sum(t))

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper('CaT'))

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

t = ['a', 'b', 'c', 'd']
x = t.pop()
# pop modifies the list and returns 
# the element that was removed. 
print(x)
print(t)

team = 'Patriots'
t = list(team)
print(t)

name = 'littlfield'

c = list(name)

print(c)

team = 'New England Patriots'
t = team.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

t = ['New', 'England', 'Patriots']
team = ' '.join(t)
print(team)