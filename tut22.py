marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)




# Python Lists
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.

print("example 1")

lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

print("ex 2")
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)


# List Index
# Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

# Example:


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]



# Accessing list items
# We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...




# Positive Indexing:
# As we have seen that list items have index, as such we can access items using these indexes.

# Example:



colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])


# Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

# Example:



print("next ex")
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])




# Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")


print("next ex")

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")



#     Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

# Syntax:

# listName[start : end : jumpIndex]

# Note: jump Index is optional. We will see this in later examples.

# Example: printing elements within a particular range:




animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'



# Example: printing all element from a given index till the end


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes



print(" printing all elements from start to a given index")


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes



#  Printing alternate values


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes


print("printing every 3rd consecutive value withing a given range")


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])




# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.



# : Accepts items with the small letter “o” in the new list

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)



# Accepts items which have more than 4 letters

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)




