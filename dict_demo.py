name = ['rose','jery','alex']
scores = [95,75,85]
i=name.index('jery')

print(scores[i])


grades = {"jery": 75, 'rose': 95}
print(grades['jery'])

grades['brian'] = 90
print(grades)

print(len(grades))
print('jery' in grades)
print(90 in grades.values())


def histogram(s):
    d = {} #could also use {}
    for c in s: #s is a string
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

bn
def print_hist(h):
    for c in h:
        print(c, h[c])
        



h = histogram('Massachusetts')
print_hist(h)


for key in sorted(h):
    h = histogram('Massachusetts')
    print(key, h[key])

#exercise 4
def storekey():
        fin = open('words.txt')
        line = fin.readline()
        word = line.strip()
        count=0
        for word in fin:
            count=len(word)
            wordcount=(word, count)
            engwords=dict(wordcount)
        


h = histogram ('bookkeeper')
print(h)