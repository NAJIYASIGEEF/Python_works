from json import load
f=open("D:\\Desktop\\Python works\\json_works\\exchange_rate\\data.json","r",encoding="utf-8")
data=load(f)


# print(len(data))

source_currency=input("Enter source currency code ")
destination_currency=input("Enter destination currency code ")

amount=int(input("Enter amount"))

conversion_rate=data.get("conversion_rates")
# print(conversion_rate)

source_currency_code_rate=conversion_rate.get(source_currency)
destination_currency_code_rate=conversion_rate.get(destination_currency)

# print(source_currency_code_rate)
# print(destination_currency_code_rate)


result=(amount/source_currency_code_rate)*destination_currency_code_rate
print(result)
