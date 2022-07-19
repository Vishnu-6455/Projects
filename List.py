# Lists: Ordered, mutbale, allows duplicate elements


mylist = ["Banana","Apple","Cherry"]
print(mylist)

#calling the values in list based on thier index value
mylist2 = [5, "apple","apple", "True"]
item = mylist[1]
print(item)

# for loop in lists
for i in mylist:
    print(i)

    #if conditions for list
    if 'apple' in mylist:
        print("yes")
    else:
        print("No")

# to check no of elements in list
print(len(mylist))

# Appending new values to list

mylist.append("Berry")
print(mylist)

mylist.insert(3, "Jamun")
print(mylist)

mylist.pop()
#print(item)
print(mylist)

mylist.remove("Jamun")
print(mylist)

mylist.reverse()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

# Multiplying a list to produce so the same values 

listmul = [1,2,3,] * 5
print(listmul)

listmul2 = [1,2,2,34,54,5,6,3]
newlist = listmul + listmul2
print(newlist)

ourlist = [1,2,3,4,5,6,7,8]
a = ourlist[1:5]
print(a)

# we can specify a step to the list using :: which would print th values by skipping the number of elements we mention. It default start from index 1 

b = ourlist[4::2]
print(b)

# copying a list 
list_org = ["banana","mango","apple"]

# Doing this way would alter the original list as well hence we use copy function/list/slicing as in line 74 to copy the list
list_cpy = list_org

list_cpy.append("lemon")
print(list_cpy)
print(list_org)

list_cpy1 = list_org.copy()
list_cpy1 = list(list_org)
list_cpy1 = list_org[:]


# creating a new list from existing list in fastest way

mylist = [1,2,3,4,5,6,7,8]
b = [i*i for i in mylist]
print(mylist)
print(b)



