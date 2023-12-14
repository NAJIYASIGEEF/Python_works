weight_kg=int(input("Enter weight in kg: "))
height_cm=int(input("Enter height in cm: "))

height_m=height_cm/100

bmi=weight_kg/height_m**2
print(bmi)

if bmi<19:
    print("underweight")
elif bmi<25:
    print("healthy")
elif bmi<30:
    print("overweight")
elif bmi<40:
    print("obesity")
elif bmi>=40:
    print("severe obese")