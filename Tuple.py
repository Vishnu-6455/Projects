# Tuple: ordered, immutable, allows duplicate elements

# Usually a tuple is created using a paranthasis however it is optional we can create a tuple without paranthasis and python
# will still consider it as a tuple

# if we are passing a one element in to the tuple then we should give , after the element otherwise it is considered as string in python

mytuple = ("Max", 28, "boston")  # mytuple = "Max", 28, "boston"
print(mytuple)

# we can convert a list into tuple
mytuple = tuple(["Max", 28 , "boston"])
item = mytuple[1]
print(item)

# Altering the values is tuple is not possible because tuple is immutable 

# mytuple[1] = "a" is not possible

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")
else:
    print("no")

my_tuple = ('a','e','i','o','u')
print(len(my_tuple))
print(my_tuple.count('o'))
print(my_tuple.index('e'))

# converting tuple to list

my_list = list(my_tuple)
print(type(my_list))

# Slicing in tuple usually same as lists so refer list file

my_tuple2 = (1,2,3,4,5,6,7,8,9,10)
b = my_tuple2[2:5]
print(b)

# unpacking a tuple

mytuple3 = "max", 28, "Hyd"

name, age , city = mytuple3

print(age)

# To unpack more than one element in a single paramter then use *. We cant use more than one * while unpacking the tuple

mytuple4 = 0,1,2,3,4,5,5,6

i1, i2, *i3, i4, i5 = mytuple4

print(i1)
print(i3)

# working with tuples is much better than working with lists because tuple consumes less space and less time to run the 
# script than that of list below are some basic calcuations to prove the statement

import sys
my_list = ["vishnu", 34, "hyd", "car"]
my_tuple3 = ("vishnu", 34, "hyd", "car")
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple3))

# Below code creates the passed list or tuple the number of times that is passed in the params
import timeit
print(timeit.timeit(stmt ="[0,1,2,3,4,5]", number = 10000000000))
print(timeit.timeit(stmt ="0,1,2,3,4,5", number = 10000000000))