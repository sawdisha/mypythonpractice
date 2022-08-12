# filter() on iterable object list

list = [5 , 6, 7, 23, 60, 1, 73, 34, 45, 3]

def check_num(num):
    if num > 30:
        return True
    else:
        return False

# filter is used to exclude items in an iterable object
greater_than_thirty = filter(check_num, list)

for i in greater_than_thirty:
    print(i)


# filter() on iterable object dictionary

dict1 = {5: "Disha", 6: "Pravin", 23:"Megha", 60:"Ahana", 1:"Bhsuhan", 73:"Raj"}

# filter on key
lesser_than_thirty = dict(filter(lambda item: item[0] <30, dict1.items()))
print(lesser_than_thirty)

# filter on  value
# __contains__ inbuilt method
h_present = dict(filter(lambda item: item[1].__contains__('h'), dict1.items()))
print(h_present)


# filter() on iterable object string

str = "Hello"

def check_char(char):
    if char == 'l':
        return True
    else:
        return False

check_l = filter(check_char, str)

for k in check_l:
    print(k)
