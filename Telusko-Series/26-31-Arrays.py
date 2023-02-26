from array import *
# or, import array as arr

# 26
# In Arrays, we need to have all the values of same type. Arrays are similar to list but
#  with one difference that u need to have all the values of same types in array
# Arrays in python don't have fixed size
# for loop makes sense when u know the range
# len(vals) gives u the length of the array

# vals = array('i', [5, 9, 8, 4, 2])
# vals = array('u', ['a', 'e', 'i'])
# print(vals.buffer_info())  #output - (2620241511,5) - 1st one address,2nd one size
# print(vals.typecode)  # variable type
# vals.reverse()

# creating a new arrau from an existing array
# newArr = array(vals.typecode, (a*a for a in vals))

# for i in range(len(vals)):
#     print(vals[i])
# /or,
# for e in newArr:
#     print(e)

# while loop in array
# i=0
# while i < len(newArr):
#     print(newArr[i])
#     i+=1


# 27 //
arr = array('i', [])

n = int(input("Enter the length of the array"))

for i in range(n):

    x = int(input("Enter the next value"))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search"))

k = 0
for e in arr:
    if e == val:
        print(k)
        break

    k += 1

print(arr.index(val))
