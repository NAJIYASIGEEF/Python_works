class Mobile:
    name:str
    brand:str
    display:str
    price:int

    def __init__(self,name,brand,display,price):
        self.name=name
        self.brand=brand
        self.display=display
        self.price=price

    def dispaly_mobile(self):
        print(self.brand,self.name,self.price)

    def __str__(self):
        return self.name

obj=Mobile("14pro","Iphone","amoled",119999)
obj2=Mobile("15pro max","Iphone","amoled",120000)
# obj.dispaly_mobile()
print(obj)
print(obj2)