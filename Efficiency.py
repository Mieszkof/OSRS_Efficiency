from Functions import *


# Input basic info
n_methods = inputInt("Input number of methods to test: ")
time_value = inputInt("Input your time's worth in gp/hr: ")
base_name = input("Input Base Name: ")
base_exp = inputInt("Input Base Exp Rate: ")
base_cost_exp = inputFloat("Input Base cost/exp (Negative rate for profit): ")
base_cost = -(base_cost_exp * base_exp)
base = [base_name, base_exp, base_cost_exp]

test_methods = []
passed_methods = [base]

for n in range(n_methods-1):
    temp_name = input("Input Method Name: ")
    temp_exp = inputInt("Input Method Exp Rate: ")
    temp_cost = inputFloat("Input Method cost/exp (Negative rate for profit): ")
    test_methods.append([temp_name, temp_exp, temp_cost])

for method in test_methods:
    name = method[0]
    exp = method[1]
    cost_exp = method[2]
    cost = -(cost_exp * exp)
    eff = ((base_cost * exp)-(cost * base_exp))/(exp - base_exp)
    if eff < time_value and exp > base_exp:

        passed_methods.append(method)
    elif eff > time_value and exp < base_exp:
        passed_methods.append(method)


passed_pairs = [(passed_methods[p1], passed_methods[p2]) for p1 in range(len(passed_methods)) for p2 in range(p1+1,len(passed_methods))]
# print(passed_pairs)

print("The most efficient method for your time value is:")
if len(passed_pairs[0]) > 1:
    winner=best_method_select(passed_pairs, time_value)
    print(winner[0], "at an exp rate of", winner[1], "per hour, Costing ", winner[2], "per exp and ", winner[2]*winner[1], "per hour.")
else:
    print(base)


