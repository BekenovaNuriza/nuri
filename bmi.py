height=int(input("enter your height:"))
weight=int(input("enter your weight:"))

bmi = weight / ( height / 100 ) ** 2

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
     print("normalweight")
elif 25 <= bmi < 30:
    print("overweight")
elif 30 <= bmi < 35:
    print("obesity class 1")
elif 35 <= bmi < 39.9:
     print("obesity class 2")
else:
     print("super")
