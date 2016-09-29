'''
result = 0
for i in range(11):
    if i % 2 == 0:
        print('current i:', i)
        result =+i # result += means result plus i

print(result)

for i in range(2,11,2):
    print('current i:', i)
    result =+i # result += means result plus i

print(result)

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print('blastoff')

countdown(5)

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


iteration = 0
while iteration < 5:
    count = 0
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

while True:
    line = input('> ')
    if line == 'done':
        break 
    print(line)

print ('done')
'''

result = 0 
i = 1
while i < 11:
    result = result + i
    i = i + 1

print(result)

result = 0 
i = 1
while i <= 10:
    if i %2 ==0:
        result +=i
    i = i + 1

print(result)

