# Dictionary" Key-Value pair, unordered, mutable

mydict = {"name":"Vis", "age": 28, "city": "hyd"}
print(mydict)

# Another way to create dictionary
mydict2 = dict(name = "vis", age = 28, city = "hyd")

mydict2["email"] = "vis.xyz.com"
print(mydict2)

# Deleting a value in Dict
del mydict["name"]
print(mydict)

mydict2.pop("age")
print(mydict2)

# to remove the lase item
mydict2.popitem()
print(mydict2)

# To check if key is in our dictionary

if "name" in mydict2:
    print(mydict2["name"])

try:
    print(mydict["name"])
except:
    print("error")

for key in mydict2.keys():
    print(key)
 
for value in mydict2.values():
    print(value)

for key, value in mydict2.items():
    print(key)
    print(value)

# Copying a dictionary
# modifying this will also modify the original hence use the same methods as in list filefff
mydict_cpy = mydict2
print(mydict_cpy)


# merging two dictionaries
my_dict = {"name":"Vis", "age": 28, "city": "hyd"}
my_dict2 = {"name":"vishnu", "age": 44, "city": "knl", "email" : "vis.xyz.com"}

my_dict.update(my_dict2)
print(my_dict)

my_dict3 = {3:9,4:5,9:7}
print(my_dict3)

# In dictionaries we can't call the values by indexes rather we call them by thier keys
print(my_dict3[3])

# We can pass a tuple as a key to the dictionary but we cant pass the list as a key because list in mutable and the key of 
# any value cant be mutable

my_tuple = 1,2,4
my_dict4 = {my_tuple: 7}
print(my_dict4)