# Defines variable of type string
formatter = "{} {} {} {}"

# prints four numericals passed for formatter variable using format function
print(formatter.format(1, 2, 3, 4))
# prints four string values passed for formatter variable using format function
print(formatter.format("one", "two", "three", "four"))
# prints keywords passed for formatter variable using format function
print(formatter.format(True, False, False, True))
# prints four variables passed for formatter variable using format function
print(formatter.format(formatter, formatter, formatter, formatter))
# prints four string statements passed for formatter variable using format function
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
