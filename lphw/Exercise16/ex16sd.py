from sys import argv

script, filename = argv

print(f"Let's read the file {filename} which was updated in the last excercise.")
updated_file = open(filename)
print(f"\nFile opened. Now read the data from file {filename} printed below:")
print(updated_file.read())
print("\nAlright, lets close this file now.")
updated_file.close()
print(f'\nFile {filename} is closed successfully')
