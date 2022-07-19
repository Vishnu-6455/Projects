# Collections: Counter, namedtuple, OrderDict, defaultdic, deque

#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

from collections import Counter
a = "aaaaaaabbbbcbcbbbb"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())

# most common counter 
print(my_counter.most_common(2))
print(my_counter.most_common(1)[0][0])


