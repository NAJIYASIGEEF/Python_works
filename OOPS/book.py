class book:
    name:str
    author:str
    pages:int
    price:int

    def __init__(self,name,author,pages,price):
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price

    def display_book(self):
        print(self.name,self.author)

    def __str__(self):
        return self.name

obj1=book("Two States","Chetan Bhagat",250,240)
obj2=book("Its ends with us","coollen Hover",160,"220")
obj3=book("Starts with us","coollen Hover",220,"250")
# obj.display_book()
print(obj1)
print(obj2)
print(obj3)
        

# id =1 update budget
# id=5 update place