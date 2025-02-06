from collections import defaultdict

# HashMaps per python'a vadinami dictionaries

# creating empty hashmap 
hashMap = {} # arba hashMap = dict()

hashMap = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

# adding a new key-value pair
hashMap["pear"] = 4

# updating existing key-value pair
hashMap["apple"] = 5

# removing a key-value pair
del hashMap["cherry"]

# checking if a key exists
if "apple" in hashMap:
    print("true")

# getting a value with a default
# my_dict.get(key, default)
value = hashMap.get("banana", 0) # output: 2
value = hashMap.get("fig", 0) # output: 0

# defaultdict: A dictionary that provides a default value for non-existent keys
# avoids KeyError and simplifies code

# creating a defaultdict with default type int
hashMap1 = defaultdict(int)

hashMap1["apple"] += 1
hashMap1["banana"] += 2
print(hashMap1)  # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})

# Creating a defaultdict with default type list
listMap = defaultdict(list)

# Adding elements
listMap['fruits'].append('apple')
listMap['fruits'].append('banana')

print(listMap)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})