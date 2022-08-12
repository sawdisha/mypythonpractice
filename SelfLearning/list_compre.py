list1 = [x.lower() for x in "HELLO"]
print(list1)

list2 = [x * x for x in range(2, 8, 2)]
print(list2)

# range(5) -> 5 elements from 0. i.e. 0, 1, 2, 3, 4
list3 = [x**4 for x in range(5) if x not in [2, 3]]
print(list3)

# list slicing format -> [start : stop : steps]
# Default value of start is 0
print(list1[1:])
print(list1[1::2])
print(list2[:2:])
