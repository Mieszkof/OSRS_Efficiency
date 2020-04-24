def inputInt(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break

def inputFloat(message):
  while True:
    try:
       userInput = float(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break


def best_method_pair_select(method_pair,threshold):
    base = method_pair[0]
    base_name = base[0]
    base_exp = base[1]
    base_cost_exp = base[2]
    base_cost = -(base_cost_exp * base_exp)
    method = method_pair[1]
    name = method[0]
    exp = method[1]
    cost_exp = method[2]
    cost = -(cost_exp * exp)
    if base == method:
        return base
    eff = ((base_cost * exp) - (cost * base_exp)) / (exp - base_exp)
    if eff < threshold and exp > base_exp:
        return method
    elif eff > threshold and exp < base_exp:
        return method
    else:
        return base


def best_method_select(method_pair_list, threshold):
    if len(method_pair_list) == 1:
        return best_method_pair_select(method_pair_list[0],threshold)
    else:
        return best_method_pair_select(
            (best_method_pair_select(method_pair_list[0],threshold),
             best_method_select(method_pair_list[1:], threshold)),threshold)

