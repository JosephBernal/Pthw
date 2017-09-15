# Var assignment of int
types_of_people = 10
# Var assignment to formatted string
x = f"There are {types_of_people} types of people."

# The actual binary joke
act_num_of_peep = 4

# Var assignment to string literals
binary = "binary"
do_not = "don't"

# Var assignment to more formatted string
y = f"Those who know {binary} and those who {do_not}."

z = f"{act_num_of_peep} is the actual number of people who know how to use binary"
# Print formatted strings
print(x)
print(y)

# Print formatted var strings
print(f"I said: {x}")
print(f"I also said: '{y}'")
print(f"I think this is the actual number: {z}")

# Joke with variable assigned to Bool
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Joke printed
print(joke_evaluation.format(hilarious))

# Concatenated strings
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
