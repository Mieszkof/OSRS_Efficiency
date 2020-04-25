from Functions import *


# Input basic info
n_methods = inputInt("Input number of methods to test: ")
time_value = inputInt("Input your time's worth in gp/hr: ")

test_methods = []

for n in range(n_methods):
    temp_name = input("Input Method Name: ")
    temp_exp = inputInt("Input Method Exp Rate: ")
    temp_cost = inputFloat("Input Method cost/exp (Negative rate for profit): ")
    test_methods.append([temp_name, temp_exp, temp_cost])

test_pairs = [(test_methods[p1], test_methods[p2]) for p1 in range(len(test_methods)) for p2 in range(p1+1,len(test_methods))]

winner=best_method_select(test_pairs, time_value)
print("\nThe most efficient method for your time value is:")
print(winner[0], "at an exp rate of", winner[1], "per hour; costing ", int(winner[2]*winner[1]), "per hour and", winner[2], "per exp.")


