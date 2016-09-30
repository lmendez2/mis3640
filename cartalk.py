#fin = open('words.txt')
#line = repr(fin.readline())
#https://docs.python.org/3/library/functions.html#repr

#fin = open('words.txt')
#for line in fin:
 #   word = line.strip()
   # print(word)


def triple_pair():
    fin = open('words.txt')
    for word in fin: 
        i = 0
        pairCount = 0
        while i <len(word) - 1:
            if word [i]== word [i+1]:
                pairCount += 1
                if pairCount == 3:
                    print(word)
                i+=2
            else:
                pairCount = 0
                i +=1
print(triple_pair())