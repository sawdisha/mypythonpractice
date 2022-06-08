from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
# hit RETURN means press Enter
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# This command is actually not needed if file is opened in 'w' mode as it will truncate the existing data from opened file by default
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Writing the file again with single line of code")
# writing command to Write all three lines in single line of code
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()
