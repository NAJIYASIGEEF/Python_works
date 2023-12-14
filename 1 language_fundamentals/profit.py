# find profit%

selling_price=int(input("Enter selling price "))
cost_price=int(input("Enter cost price "))

profit=selling_price-cost_price
print(f"profit = {profit}")

profit_perc = (profit/cost_price)*100
print(f"A product whose cost price is {cost_price} sold for rupees {selling_price} then profit % ={profit_perc}")