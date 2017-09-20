# This is the initial creation of the function where cheese_and_crackers is assigned two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Here is where we output some strings
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# The reason this prints as the first line is because this is an actual statement outside the defining of the function
print("We can just give the function numbers directly:")

# Here we invoke cheese_and_crackers with two individual variables
cheese_and_crackers(20, 30)

# Here we assign values to the variables directly
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Then we invoke those variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Here we can add values together in the variable call
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Here we can add values to variables in a seemingly mixed way. However since the variables contain integers both data types are the same and add as such.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def winning(luck, perseverance):
    print(f"Winning is {luck} % luck and {perseverance} % perseverance. \n")

winning(10, 90)

luck = 10
perseverance = 100
winning(luck, perseverance)

luck = perseverance - luck
perseverance = perseverance + perseverance
winning(luck, perseverance)

winning(amount_of_cheese * amount_of_crackers, luck)
