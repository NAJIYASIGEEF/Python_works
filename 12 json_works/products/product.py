from json import load
f=open("D:\\Desktop\\Python works\\jason_works\\products\\items.json","r",encoding="utf-8")
data=load(f)

# print(len(data))

# print all category
categories={p.get("category") for p in data}
print(categories)

electronic_products=[p for p in data if p.get("category")=="electronics"]
# print(len(electronic_products))

jwellery_products=[p for p in data if p.get("category")=="jewelery"]
print(len(jwellery_products))

