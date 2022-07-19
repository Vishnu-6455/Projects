# Set: unordered, mutable, no duplicates

# Below are the methods to create a set
myset = {1,2,3,4,5}
myset = set([1,2,3,4,5])
mysetstr = set("hello")
print(type(mysetstr))
print(mysetstr)

# To create a empty set we cant create using a flower bracket because it will be recognised as a dictionary than a set
# hence we create that in the following way

mysetemp = set()

# Adding and removing elements in set

myset.add(88)
myset.add(00)

print(myset)

# This method will remove the element if it is present in the set else throws an error
# hence use discard function which will remove if the element is there or else does nothing basically doesn't throw any error
myset.remove(00)
print(myset)

myset.discard(77)
print(myset)

# Poping elements in set
print(myset.pop())

for i in myset:
    print(i)

if 1 in myset:
    print("yes")
else:
    print("no")

# union and intersection in sets
odds = {1,3,5,7,9}
even = {0,2,4,6,8,}
prime = {2,3,5,7}

u = odds.union(even)
print(u)

i = odds.intersection(prime)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

# The  difference function will output the elements in A other than the one's in common
diff = setA.difference(setB)
print(diff)

# The symmetric difference function will output the all the elements in both the sets other than the one's in common
diff1 = setA.symmetric_difference(setB)
print(diff1)

# Adds the elements to the sets without adding the duplicate elements
setA.update(setB)
print(setA)

# updates only the intersection/diff elements
setA.intersection_update(setB)
print(setA)
setA.difference_update(setB)
print(setA)

# Subset and Superset
set1 = {1,2,3,4,5,6}
set2 = {1,2,3}
set3 = {7,8}

print(set1.issubset(set2))
print(set2.issubset(set1))

print(set1.issuperset(set2))
print(set2.issuperset(set1))

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))

# Copying sets conecpt follows the same as lists so refer list file


# FORZEN SET it is a immutable version of a set

a = frozenset([1,2,3,4,])
a.remove(1) # This wont work



