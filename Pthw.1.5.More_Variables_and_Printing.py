name = 'Zed A. Shaw'
age = 35 # not a lie
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# height
height = 74 # inches
cm_per_inch = 2.54
height_cm = height * cm_per_inch # conversion cm --> in

# weight
weight = 180 # lbs
kg_per_lb = 0.453592
weight_kg = weight * kg_per_lb # conversion lbs --> kg


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this liine is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"His height in centimeters is {height_cm} and his weight in kilograms is {weight_kg}.")
