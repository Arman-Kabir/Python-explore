
# Python OOP Concepts
# Attributes and Objects  # Method Kinds  # Encapsulation  # Abstraction  # Polymorphism  # Abstract Classes  # Store management system

# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
#
# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))

# In Python , Each data type is an object that has been instantiated earlier by some class and for the item1 variablethat has been instantiated
# from a string type of class. And for the price_quantity and price_total that have been instantiated from a class named int means integer.

# We can create a data type of our own, it would allow us to write a code that we can re-use in the future easily if needed.
# Now, each instance could have attributes to describe related information about it.


# 3m40s
# It's going to be divided into 2 parts. 1st one of the equation of the class, 2nd one  will be the part i instantiate some object of this class
# Method is function inside classes. When we create function inside classes - then it's called method.

class Item:
    def calculate_total_price(self,x,y):
        return x*y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price,item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price,item2.quantity))


# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# random_str = "aaa"
# print(random_str.upper())





