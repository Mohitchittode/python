# Dictionary Methods
# Dictionary uses several built-in methods for manipulation.They are listed below

# update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1) 



print("next code ")

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)


# Removing items from dictionary:
# There are a few methods that we can use to remove items from dictionary.

# clear():
# The clear() method removes all the items from the list.

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)


# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.

# Example:


info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)



# popitem():
# The popitem() method removes the last key-value pair from the dictionary


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)


# del:
# we can also use the del keyword to remove a dictionary item.

# Example:


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)


# If key is not provided, then the del keyword will delete the dictionary entirely.


# Example:


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)