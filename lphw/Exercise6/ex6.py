# assigning a numerical value to the variable
types_of_people = 10;
# created f-string to use variable inside string
x = f"There are {types_of_people} types of people."

# assigned string values to two variables
binary = "bianay"
do_not = "don't"
# used multiple variables inside f-string
y = f"Those who know {binary} and those who {do_not}."

# printed both f-strings
print(x)
print(y)

#used f-string inside print function
print(f"I said: {x}")
print(f"I also said: '{y}'")

# created a boolean variable
hilarious = False
# created second type of formated string
joke_evaluation = "Isn't that joke so funny?! {}"

# variable is added in string using .format() synatx
# This gives developer a scope to use different variables inside a strings depending on user input
# Example we can have another variable 'is_hilarious = True' and we can use it the print function depending on user's reaction
# i.e. print(joke_evaluation.format(is_hilarious))
print(joke_evaluation.format(hilarious))

w = "This is a left side of..."
e = "a string with a right side."

# Python uses + to concatenate strings
print(w + e)
