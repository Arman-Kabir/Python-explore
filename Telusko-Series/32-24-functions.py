# 32  // Functions
def greet():
    print("Hello")
    print("Dg morn")


def add_sub(x, y):
    c = x+y
    d = x-y
    return c, d


greet()
result1, result2 = add_sub(5, 4)
print(result1, result2)
