mobile={"id":100,"name":"iphone","price":100000,"imei":2345,"processor":"apple"}

# print all key value pairs
# for k,v in mobile.items():
#     print(k,v)

# print name
print(mobile.get("name"))

# print price
print(mobile.get("price"))

# update price =85000
mobile.update({"price":85000})
print(mobile)

# remove imei
mobile.pop("imei")
print(mobile)

# add a key and value
mobile["offer"]=1000
print(mobile)

# mobile.update({"offer":10000})
# print(mobile)

mobile["price"]+=1000       #price+1000
print(mobile)

print("color" in mobile)