# form {key: value for (key, value) in iterable }

keys = ['p', 'q', 'r', 's', 't', 'u']
values = [3, 4, 8, 2, 9, 1]
dummy_list = ["dnd", "ncldckmdl", "ddhcod"]

# using tuple() to display readable version of zip object
print(tuple(zip(keys, values)))

print(tuple(zip(keys, values, dummy_list)))
# output -> (('p', 3, 'dnd'), ('q', 4, 'ncldckmdl'), ('r', 8, 'ddhcod'))

# first way
my_dict = {keys:values for (keys, values) in zip(keys, values)}
print(my_dict)

# second way
my_new_dict = dict(zip(keys, values))
print(my_new_dict)

# third way
my_other_dict = {x: x**3 for x in [1, 2, 3, 4, 5, 6]}
print(my_other_dict)

# forth way
my_another_dict = {k: v for (k,v) in zip("HELLO", "disha")}
print(my_another_dict)

# fifth way
my_new_another_dict = {ks: vs for (ks,vs) in zip("HELLO", ("disha", "raj", "bhushan", "padma", "prachi"))}
print(my_new_another_dict)

# sixth way
# dictionary comprehension with if
# range(start, stop, step)
# range start from 0
my_new_other_dict = {x: x**2 for x in range(1, 10) if x % 2 == 0}
print(my_new_other_dict)
