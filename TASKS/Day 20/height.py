# 2. Write a program to filter the dictionary, from a dictionary of people’s heights and you wanted to filter out anyone below a certain height.
# Let’s filter out anyone less than 170cm.

heights={"Alice":155,"Anna":161,"Sam":173,"Mohan":172,"Malu":156,"Ali":179,"Sara":157,"Sana":170}

for name,height in heights.items():
    if height>=170:
        print(f"{name}: {height}")



