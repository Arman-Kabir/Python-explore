# 32  // Functions
# def greet():
#     print("Hello")
#     print("Dg morn")


# def add_sub(x, y):
#     c = x+y
#     d = x-y
#     return c, d


# greet()
# result1, result2 = add_sub(5, 4)
# print(result1, result2)


# 33 //Functions Arguments
# *Pass By value     *Pass by reference
# Integer , Strings - they are immutable
def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print(x)


a = 10
print(id(a))
update(a)
print('a', a)
