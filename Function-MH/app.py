# round(),print()
# def-- used for define function... print()--> takes an input.
# Paramater is input that define your function, argument is the actual value for a given parameter.

# def greet(fn, ln):
#     print(f"Hi{fn}{ln} ")
#     print("Welcome aboard")
# greet("Mosh", "Hamedani")
# greet("John")

# In programming, we have 2 types of functions...1- Perform a task... 2- Calculate and return a value.
# In python - All functions by default return a none value.None is an object that represents absence of a value.

def increment(number, by):
    return number+by

print(increment(2,by=1)) #keyword argument
    
