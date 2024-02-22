# Python Sets
# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

harry = set()
print(type(harry))

for value in info:
  print(value)

#  Accessing set items:
# Using a For loop
# You can access items of set using a for loop.

# Example:


info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)



    