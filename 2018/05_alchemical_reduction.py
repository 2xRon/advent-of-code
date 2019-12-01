"""
ADVENT OF CODE: 2018
Day 5: Alchemical Reduction
"""

polymer = open("inputs/05.input", "r").read().strip()
# polymer = 'dabAcCaCBAcCcaDA'
def react_polymer(polymer):
    polymer += "_"
    while True:
        polymer_new = ""
        it = iter(range(len(polymer) - 1))
        for idx in it:
            if abs(ord(polymer[idx]) - ord(polymer[idx + 1])) != 32:
                polymer_new += polymer[idx]
            else:
                next(it, None)
        polymer_new += polymer[-1]
        if polymer == polymer_new:
            break
        polymer = polymer_new
    return polymer[:-1]


# part 1
print(len(react_polymer(polymer)))

# part 2
charset = set(c for c in polymer.lower())
print(
    min(
        len(react_polymer(polymer.replace(c, "").replace(c.upper(), "")))
        for c in charset
    )
)
