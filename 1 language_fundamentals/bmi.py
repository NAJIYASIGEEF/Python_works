# calculate bmi

weight_in_kg=int(input("Enter weight in kg "))
height_in_cm=int(input("Enter height in cm "))

height_in_meter= (height_in_cm/100)

bmi = weight_in_kg/(height_in_meter**2)
print(f"Body Mass Index (BMI) = {bmi}")