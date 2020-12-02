"""
AOC 2019
Day 14: Space Stoichiometry
Solution by 2xRon
"""

import re
from collections import defaultdict
from math import ceil

def smallest_greater_multiplier(a,b):
    # smallest integer k st k*a >= b
    return ceil(b/a)

# assumes each reaction has only one product, each product has only one producing reaction, ORE consuming reactions only have one product
reactants = list()
products = list()
# with open("inputs/14.input") as in_file:
with open("./testf") as in_file:
    for line in in_file.readlines():
        reactant, product = line.split(" => ")
        reactants.append([(x.split(" ")[1],int(x.split(" ")[0])) for x in reactant.strip().split(", ")])
        products.append((product.strip().split(" ")[1],int(product.strip().split(" ")[0])))

reaction_products = [x[0] for x in products]
def get_reaction(ingredient):
    return reaction_products.index(ingredient)
fuel_idx = get_reaction("FUEL")

required_ingredients = defaultdict(int, reactants[fuel_idx])
required_ore = 0
print(required_ingredients)
while required_ingredients:
    product, required_prod_qty = required_ingredients.popitem()
    product_stoich = products[get_reaction(product)][1]
    n_reactions = smallest_greater_multiplier(product_stoich, required_prod_qty)
    for reactant, reactant_stoich in reactants[get_reaction(product)]:
        if reactant != "ORE":
            required_ingredients[reactant] += n_reactions*reactant_stoich
        else:
            required_ore += n_reactions*reactant_stoich
    print(required_ingredients, '\n')
    input()

print("Part 1:",required_ore)




