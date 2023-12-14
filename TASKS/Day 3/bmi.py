# 3. Write a program to calculate BMI and give message ‘’over weight,underweight,healthy’’

height=int(input("Enter height in cm:"))
weight=int(input("Enter weight in kg:"))

height_in_m=height/100
height_meters=height_in_m**2

bmi=weight/height_meters

print(bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>18.5 and bmi<24.9:
    print("Normal")
elif bmi>25 and bmi<29.9:
    print("Overweight")
elif bmi>30 and bmi<34.9:
    print("obese")
elif bmi>35:
    print("Extremely obese")