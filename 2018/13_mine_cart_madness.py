"""
ADVENT OF CODE: 2018
Day 13: Mine Cart Madness
"""

from itertools import cycle, product, chain
from copy import deepcopy

in_file = open("inputs/13.input", "r").read().strip("\n")

# Symbol Mappings
cart_replacement = dict([(">", "-"), ("<", "-"), ("v", "|"), ("^", "|")])
cart_symbol_direction = dict([(">", 1), ("<", -1), ("v", 1j), ("^", -1j)])
cart_direction_representation = {v: k for k, v in cart_symbol_direction.items()}
bend_direction_horz = dict([("\\", 1j), ("/", -1j)])
bend_direction_vert = dict([("\\", -1j), ("/", 1j)])


# Symbol sets
CART_SYMBOLS = "><v^"
BEND_SYMBOLS = "\\/"
INTERSECTION = "+"
VERT = "|"
HORZ = "-"

line_split = in_file.split("\n")
mine_list = [list(l) for l in line_split]


class Mine:
    carts = list()
    crashes = list()
    ticks = 0

    def _find_carts(self, dirty_mine):
        for r, c in product(range(self.height), range(self.width)):
            s = dirty_mine[r][c]
            if s in CART_SYMBOLS:
                self.carts.append(Cart(c + r * 1j, s))
                dirty_mine[r][c] = cart_replacement[s]
        return dirty_mine

    def collide(self, next_pos):
        self.crashes.append(next_pos)

    def __init__(self, mine_with_carts):
        self.height = len(mine_with_carts)
        self.width = len(mine_with_carts[0])
        self.mine_list = self._find_carts(mine_with_carts)

    def __getitem__(self, index: complex):
        return self.mine_list[int(index.imag)][int(index.real)]

    def __setitem__(self, index: complex, value: str):
        if len(value) != 1:
            raise ValueError("One character per tile")
        self.mine_list[int(index.imag)][int(index.real)] = value

    def __iter__(self):
        return self

    def __next__(self):
        for cart in sorted(self.carts):
            cart.advance(self)
        self.ticks += 1
        return self.ticks

    def __repr__(self):
        with_carts = deepcopy(self.mine_list)
        for cart in self.carts:
            with_carts[int(cart.y)][int(cart.x)] = cart_direction_representation[
                cart.direction
            ]
        for crash in self.crashes:
            with_carts[int(crash.imag)][int(crash.real)] = "X"
        return "\n".join("".join(x) for x in with_carts)


class Cart:
    def __init__(self, pos: complex, symbol: str):
        self.pos = pos
        self.direction = cart_symbol_direction[symbol]
        self.next_turn = cycle([-1j, 1, 1j])  # Left, Straight, Right
        self.crashed = False

    def turn(self):
        turn_direction = next(self.next_turn)
        self.direction *= turn_direction

    @property
    def next_pos(self):
        return self.pos + self.direction

    def check_collide(self, next_pos: complex, mine: Mine):
        for cart in mine.carts:
            if next_pos == cart.pos and not cart.crashed:
                self.crashed = True
                cart.crashed = True
                mine.collide(next_pos)
                return True
        else:
            return False

    def advance(self, mine: Mine):
        if self.crashed:
            return
        next_pos = self.next_pos
        next_type = mine[next_pos]
        if self.check_collide(next_pos, mine):
            self.pos = next_pos
            return self.pos
        if next_type in BEND_SYMBOLS:
            if mine[self.pos] == HORZ:
                self.direction *= bend_direction_horz[next_type]
            elif mine[self.pos] == VERT:
                self.direction *= bend_direction_vert[next_type]
            elif mine[self.pos] == INTERSECTION:
                if self.direction.imag != 0:  # vert
                    self.direction *= bend_direction_vert[next_type]
                else:
                    self.direction *= bend_direction_horz[next_type]
            self.pos = next_pos
        if next_type in INTERSECTION:
            self.pos = next_pos
            self.turn()
        else:  # Straight
            self.pos = next_pos
        return

    @property
    def _key(self):
        return (self.pos.imag, self.pos.real)

    def __lt__(self, other):
        return self._key < other._key

    def __eq__(self, other):
        return self._key == other._key

    @property
    def x(self):
        return self.pos.real

    @property
    def y(self):
        return self.pos.imag

    def __repr__(self):
        return f"Position: {self.x},{self.y}, Direction: {cart_direction_representation[self.direction]}, Crashed: {self.crashed}"


# Complete parts A and B
verbose = False
this_mine = Mine(mine_list)
if verbose:
    print(this_mine)
for tick in this_mine:
    if verbose:
        print(this_mine.carts)
        print(tick)
        print(this_mine)
    if len(this_mine.crashes) == 1:
        partA = this_mine.crashes[0]
    uncrashed_carts = [cart for cart in this_mine.carts if not cart.crashed]
    if len(uncrashed_carts) == 1:
        partB = uncrashed_carts[0].pos
        break

print("Part A: " + f"({int(partA.real)},{int(partA.imag)})")
print("Part B: " + f"({int(partB.real)},{int(partB.imag)})")
