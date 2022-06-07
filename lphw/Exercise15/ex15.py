#Getting argv module from sys package
from sys import argv

# assigning variables to argv to pass filename as a argument
script, filename = argv

# storing command to open file in txt file object
txt = open(filename)

# printing text file name using f-String
print(f"Here is your file {filename}:")
# read the data from text file opened in the txt variable
print(txt.read())
txt.close()

print("Type the filename again:")
# take filename as input from user
file_again = input("> ")

#Storing command to open file in new file object
txt_again=open(file_again)

# printing data from opened file`
print(txt_again.read())
txt_again.close()
