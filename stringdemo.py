team = "new york yankees"
print(team[0])

print(len(team))

print(team[len(team)-1])
last = team[-1]
print(last)

index = 0
while index < len(team):
    letter = team[index]
    print(letter)
    index += 1 #prints a letter in every line 

for letter in team:
    print(letter)  #same just simpler for every letter in team = yankees it is printed 

prefix = 'jklmnopq'
suffix = 'ack'
for letter in prefix:
    if letter == 'o' or letter == 'q':
        suffix = 'uack'
    else:
        suffix = 'ack'
    print(letter +suffix)

print (team[0:11])
print (team[12:20])
print (team[12:])
