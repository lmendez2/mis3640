
weight = 108
height = 63**2
bmi = (weight/height) * 703
print('your weight is', weight)
print('your height is', height)
print('your bmi is', bmi)

if bmi >= 30:
    print("you are obese", bmi)
elif 25 <= bmi < 30:
    print("you are overweight", bmi)
elif 18.5 <= bmi <25:
    print("you are normal weight", bmi)
else bmi < 18.5:
    print("you are underweight", bmi)






input()



def factorial(n):
    if n == 1:
        return 1
    print('current n =', n) 
    return n * factorial(n - 1)


print(factorial(1))
print(factorial(3))



def fibonacci(n):
    if n==0 or n ==1:
        return 1 #result under n = 1 or 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(20))

def gcdRecur(a, b):

    print('Current a, b:', a, b) 
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


print(gcdRecur(9,12))