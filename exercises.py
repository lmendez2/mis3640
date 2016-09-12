import time 
print (time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
hours = (current//60)//60 % 24
days = current// 60 //60 //24
print('curent time: %d days, %d hours, %d minutes and %d seconds from Epoch.' % (days, hours, minutes, second))

#wrong attempt because my math is bad
#print((time.time()/60), 'minutes')
#print((time.time()/60/60), 'hours')
#print((time.time()/60/60/24), 'days')
#print((time.time()/60/60/366), 'years')

input()