# Var assignment of int
types_of_people = 10
# Var assignment to formatted string
x = f"There are {types_of_people} types of people."

# Var assignment to string literals
binary = "binary"
do_not = "don't"

# Var assignment to more formatted string
y = f"Those who know {binary} and those who {do_not}."

# Print formatted strings
print(x)
print(y)

# Print formatted var strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Joke with variable assigned to Bool
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Joke printed
print(joke_evaluation.format(hilarious))

# Concatenated strings
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
