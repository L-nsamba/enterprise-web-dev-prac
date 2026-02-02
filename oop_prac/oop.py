# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year =  year
    
#     def get_summary(self):
#         print(f"""
#         Title: {self.title}
#         Author: {self.author}
#         Year: {self.year}
#         """)

# Book_One = Book("ROBIN HOOD", "Arnold Shepred", 1998)

# Book_One.get_summary()

# class Car():
#     def __init__(self, name, color, year):
#         self.name = name
#         self.color = color
#         self.year = year

#     def get_car_info(self):
#         print(f"""
#         Car Name: {self.name}
#         Car Color: {self.color}
#         Production Year: {self.year}
# """)
        
# Car_One = Car("Rolls Royce", "orange", 2020)
        
# Car_One.get_car_info()



class Groceries():
    def __init__(self, name, price, expiry_date):
        self.name = name
        self.price = price
        self.expiry_date = expiry_date

    def get_grocery_info(self):
        print(f"""
        Item Name: {self.name}
        Price: {self.price}
        Expiry Date: {self.expiry_date}
""")

item_one = Groceries("Pilau", 23000, "02/20/2026")
item_two = Groceries("Eggs", 4000, "01/02/2026")

item_one.get_grocery_info()
item_two.get_grocery_info()

