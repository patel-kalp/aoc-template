#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf

import collections 
import math
import re

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
engine_parts = collections.defaultdict(list) 
engine_schematic = list(input)
board = engine_schematic

symbols = set()
# Iterate through each cell of the engine schematic
for row in range(len(input)):
    for col in range(len(input[0])):
        # If the value of the cell if a symbol (*, #, +, ..)
        # add the coordinates in the symbols set
        if list(input)[row][col] not in '.1234567890':
            symbols.add((row, col))

for row_num, row_val in enumerate(engine_schematic):
    # Using regex finditer will find all the occurances of a number or a set of consecutive numbers in the given row (row_val)
    
    # Let's say the current row_val is .123..4..56
    # Given that row m will find [123, 4, 56] and iterate through each
    # Here m will be the match (123) and the span of m will be it's starting and ending coords (1,4) [inclusive_start, exclusive_end]

    for m in re.finditer(r'\d+', row_val):
        neighboring_cells = set()
        # Given the match (number), get coords of the neighboarding cell in a 3 by 3 grid and adds that to the set of neighboarding cells
        for r_offset in (-1, 0, 1):
            for c_offset in (-1, 0, 1):
                for c_index in range(*m.span()):
                    neighboring_cells.add((row_num + r_offset, c_offset + c_index))
        
        # Then for each of the coordinates in the sets, add matched digits to the corresponding key in the engine_parts dictionary
        for i in neighboring_cells & symbols:
            engine_parts[i].append(int(m[0]))

ans = 0
for p in engine_parts.values():
    ans += sum(p)

print("Answer A:", ans)

# part b
ans = 0
for p in engine_parts.values():
    if len(p) == 2:
        ans += math.prod(p)

print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
