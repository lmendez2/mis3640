def all_factors(x):
    """
finding the factors of an integer
    """         
    for i in range (1, x+1):
        if x % i == 0: #we find which number divides with zero remainder        
            print (i); #for numbers with zero remainder we print 

x = int(input('enter an integer')) #asking the user for the input

print(all_factors(x))
