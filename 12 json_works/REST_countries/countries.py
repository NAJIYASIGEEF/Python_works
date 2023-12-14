from json import load
f=open("D:\\Desktop\\Python works\\jason_works\\REST_countries\\data.json","r",encoding="utf-8")
data=load(f)

print(len(data))

# 1 print all country names

all_country_names=[c.get("name") for c in data]
# print(all_country_names)


# 2 independent country names

inde_con=[c.get("name") for c in data if c.get("independent")==True]
# print(inde_con)


# 3 print all regions

all_region={c.get("region") for c in data }
# print(all_region)


# 4 print all asian country names

asian_region=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_region)


# 5 capital of ukraine

cap_ukraine=[c.get("capital") for c in data if c.get("name")=="Ukraine"]
# print(cap_ukraine)

# 6 print all country names and capitals

capitals=[(c.get("name"),c.get("capital")) for c in data]
# print(capitals)

# 7 country name and currency

for c in data:
    if "currencies" in c:
        curr_data=c.get("currencies")[0]
        # print(curr_data)
        # print(curr_data.get("name"),",", c.get("name"))


# 8 borders of india

india_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]
# print(india_borders)
india_border_names=[c.get("name") for c in data if c.get("alpha3Code") in india_borders]
# print(india_border_names)


# 9 country name with more than 4 borders


for c in data:
    if "borders" in c and len(c.get("borders"))>4:
        print(c.get("name"))
      


    