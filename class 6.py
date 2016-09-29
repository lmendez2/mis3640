
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

