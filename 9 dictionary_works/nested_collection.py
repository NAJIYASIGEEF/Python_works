vehicles=[
   
    {"id":1,"name":"passion pro","brand":"hero","price":100000},
    {"id":2,"name":"xpulse","brand":"hero","price":140000},
    {"id":3,"name":"trumph","brand":"triumph","price":300000},
    {"id":4,"name":"hunter","brand":"royal","price":200000},
    {"id":5,"name":"ola s1","brand":"ola","price":170000},
    {"id":6,"name":"ather 400","brand":"ather","price":180000},

]

# for bike in vehicles:
#     print(bike.get("name"))             #get all the names of bikes

# for bike in vehicles:
#     print(bike.get("brand"))

# for bike in vehicles:
#     if bike.get("brand")=="hero":
#         print(bike.get("name"))           #display bike brand with hero


# for bike in vehicles:
#     if bike.get("price")<150000:
#         print(bike.get("name"))           # bikes available under 150000

# costly bike
bike_list=[]
for bike in vehicles:
    bike_list.append(bike.get("price"))
    max_price=max(bike_list)
# print(max_price)
for bike in vehicles:
    if bike.get("price")==max_price:
        print(bike)


# or
costly_bike=max(vehicles,key=lambda d:d.get("price"))
print(costly_bike)

low_cost=min(vehicles,key=lambda d:d.get("price"))
print(low_cost)


                






