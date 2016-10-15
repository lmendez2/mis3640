"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.
Among them, three were telling the truth while one was lying.
Could you find out who is the thief?
"""
for theif in ['john', 'paul','george','ringo']:
    sum = (theif != 'john') + (theif == 'george') + (theif == 'ringo') + (theif != 'ringo') #the theif is or is not equal to test the iterations 
    if sum == 3: #sums up the truths
        print('the theif is {}.' .format(theif))