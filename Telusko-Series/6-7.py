
# 6 //
# Tuple is almost same as list. U can have different of values there.
# Difference is -- In list, we can change values means list is mutable and tuple is immutable means
#  we can't change the values.   ---- [] used in list and () used in tuple.
# Since we do not change values in tuple - iteration in tuple is faster than list

tup = (21, 36, 14, 25)
# tup[1] = 33    // 'tuple' object does not support item assignment
# print(tup.count())
# print(tup[1])

# Set -- set never follows a sequence. - set uses concepts of hash. Using hash we improve the performance
# In set , indexing is not supported
# s = {22, 25, 14, 21, 5}
# print(s)


# Recap --- List,Tuple,set
# List is a collection of values.This can be of different types or same types.
# Tuple is same as list - in tuple, we can not change values cz they are immutable
# Set is almost same as list .Difference is it will not maintain the sequence.Will not support duplicate
# values




# //////New video - Dictionary -   key-value pairs. {}used in dictionary.  Key should be 
# immutable and unique. We can use strings,numbers as keys.
# when fetching value from Dictionary - []used to mention key

# data = {1: 'Navin', 2: 'Kiran', 4: 'Harsh'}
# print(data[2])
# print(data.get(1,'Not found'))
# print(data.get(3,'Not found'))

# Create a dictionary with the help of list
keys = ['Navin','Kiran','Harsh']
values = ['Python','Java','JS']

data1 = dict(zip(keys,values))
data1['monika'] = 'cs'
print(data1)
print(data1['Kiran'])

prog = {'JS':'Atom','CS':'VS','Python':['PyCHarm','Sublime'],'java':{'JSE':'NetBeans','JEE':'Eclipse'}}
print(prog['JS'])
print(prog['Python'][1])
print(prog['java']['JEE'])
