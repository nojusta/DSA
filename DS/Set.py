# creating an empty set
my_set = set() # arba my_set = {}

my_set = {1, 2, 3, 4}

# adding an element
my_set.add(5)

# removing an element
my_set.remove(3)

# checking
print(3 in my_set) # false, nes panaikinom
print(4 in my_set) # true

# set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union
union_set = set1 | set2
print(union_set) # output {1, 2, 3, 4, 5}

# intersection
intersection_set = set1 & set2
print(intersection_set) # output {3}

# difference
difference_set = set1 - set2
print(difference_set) # output {1, 2}

# symmetric difference 
sym_diff_set = set1 ^ set2
print(sym_diff_set) # output {1, 2, 4, 5}

# update
set1.update(set2) # arba set1 |= set2

print(set1) # output {1, 2, 3, 4, 5} 
print(set2) # output {3, 4, 5} (nepasikeite)