from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    print(f.seek(0))

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

# example 1
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print("Rewinding again!")
rewind(current_file)

# example 2 using for loop
print(f"Trying for loop to print first 4 lines from file {input_file}")

for count in range(1, 5):
    print_a_line(count, current_file)

print("Rewinding once again!")
rewind(current_file)

# example 3 using while loop and shorthand notation
count_line = 1

print(f"Printing first 2 lines from file {input_file}")
while count_line < 3:
    print_a_line(count_line, current_file)
    count_line += 1

print("All done!")
