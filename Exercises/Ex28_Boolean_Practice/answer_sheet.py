True and True: True
False and True: False
1 == 1 and 2 == 1: False
"test" == "test": True
1 == 1 or 2 != 1: True
True and 1 == 1: True
False and 0 != 0: True
True or 1 == 1: True
"test" == "testing": False 
1 != 0 and 2 == 1: False
"test" != "testing": True
"test" == 1: False
not (True and False): True 
not (1 == 1 and 0 != 1): False 
not (10 == 1 and 0 != 1): True
not (10 == 1 or 1000 == 1000): False
not ("testing" == "testing" and "Zed" == "Cool Guy"): True
1 == 1 and (not ("testing == 1 or 1 == 0")): True
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)): True
3 == 3 and (not ("testing" "testing" or "Python" == "Fun")): 
: 
# Tips:: 
# 1. Find an equality test (== or !=) and replace it with its truth.: 
# 2. Find each and/or inside parentheses and solve those first.: 
# 3. Find each not and invert it.: 
# 4. Find any remaining and/or and solve it.: 
# 5. When you are done you should have True or False.: 
