product={"code":1000,"name":"Orange","price":35}

print(product["name"])              #returns error if not present

for k in product.keys():            #return keys
    print(k)

# values()
for v in product.values():          #return values
    print(v) 

# items()
for k,v in product.items():         #return key and values
    print(k,v)

# get()
print(product.get("name"))          #doesnt display error if we entered the wrong key

#updating the value of key 
product["price"]=50
# print(product)

# update()
product.update({"name":"apple"})        #update using update()
print(product)

# pop()
product.pop("price")
print(product)




