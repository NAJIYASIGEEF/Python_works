# 2.	Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units      No charge
# Next 100 units     Rs 5 per unit
# After 200 units    Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000
units=int(input("Enter consumed no.of units:"))
# total_bill_amount=rate_unit*units+fixed_amount
first_100_unit=0
next_100_unit=5
after_200_unit=10
if units<=100:
    total_bill_amount=first_100_unit
elif units <100 and units <=200:
    total_bill_amount=first_100_unit + (units - 200) * next_100_unit
else:
     total_bill_amount = first_100_unit + 100 * next_100_unit + (units - 200) * after_200_unit
print(f"Total bill amount: {total_bill_amount}")
