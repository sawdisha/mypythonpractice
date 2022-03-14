name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # inces
cm_height = 2.54 * height
weight = 180 # lbs
kg_weight = weight/2.2046
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall which is {cm_height} centimeters.")
print(f"He's {weight} pounds heavy which is {round(kg_weight,2)} kilogorams.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f'His teeth are usually {teeth} depending on the coffee.')

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
