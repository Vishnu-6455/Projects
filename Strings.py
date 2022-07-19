# Strings: ordered, immutbale, text representation
# We can use either single or double quotes 
# Triple quotes are used for multiple statements
# Giving forwardslash(\) after a word will give the whole statement in single line though we write it as a paragraph

from timeit import default_timer as timer
my_string = "Hello World"
print(my_string)

# Accesing a character, we cant change the character as it is immutable
char = my_string[3]
print(char)

# same as lists
print(my_string[1:5])

# Reversing a slit using slicing operator
print(my_string[::-1])

# concatenation of strings
name = "Tom"
sentence = my_string+' '+name
print(sentence)

for i in my_string:
    print(i) 

if 'h' in my_string:
    print("yes")
else:
    print("no")

mystring = '     Hello World     '
# to remove the above whitespaces in the string
mystring = mystring.strip()
print(mystring)

# converting to upper and lower 
print(mystring.upper())
print(mystring.lower())

print(mystring.startswith('H'))
print(mystring.endswith('orld'))
print(mystring.casefold())
print(mystring.find('o'))
print(mystring.replace("World", "universe"))

# converting string to list and converting back to string
mystring1 = "how are you doing"
my_list = mystring1.split()
print(my_list)

new_string = ' '.join(my_list)
print(new_string)

mylist3 = ['a'] * 10000000
#print(mylist3)

#bad method to conver to string
start = timer()
mystring2 = ''
for i in mylist3:
    mystring2 += i
stop = timer()
print(stop-start)
#print(mystring2) 

# good menthod to conver to string
start = timer()
mystring2 = ''.join(mylist3)
stop = timer()
print(stop-start)
#print(mystring2)

# Formatting strings 
# %, .format(), f-strings

var = "Tom"
var2 = "vis"
mystring4 = " the varaible is {}".format(var)
print(mystring4)
mystring = f"the variable is {var*2} and {var2}"
print(mystring)
