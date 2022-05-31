from sys import argv
script, name, city = argv

print("The script is:", script)
print("My name is:", name)
print("I live in:", city)
print("Okay, great! What's your hobby?", end=' ')
hobby = input()
job = input("And your dream job is? ")
print(f"Awesome {name}! All the best for your {job} job search. Enjoy {hobby}.")
