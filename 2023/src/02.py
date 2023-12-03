#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

red_max, green_max, blue_max = 12, 13, 14

def find_max_cubes_per_color(input):
    max_cubes_per_game = {}

    for i, line in enumerate(input):
        line = line[line.index(":")+2:] # Get rid of Game X:
        cubes = [x.strip() for x in line.replace(";", ",").split(",")]
        
        red, green, blue = 0, 0, 0
        for cube in cubes:
            x = cube.split(" ")
            if x[1] == "red" and int(x[0]) > red:
                red = int(x[0])
            elif x[1] == "green" and int(x[0]) > green:
                green = int(x[0])
            elif x[1] == "blue" and int(x[0]) > blue:
                blue = int(x[0])
        max_cubes_per_game[i + 1] = [red, green, blue]
    return max_cubes_per_game
        

# part a
ans = 0
max_cubes_per_game = find_max_cubes_per_color(input)
for game in max_cubes_per_game.keys():
    red, green, blue = max_cubes_per_game[game]
    if red <= red_max and green <= green_max and blue <= blue_max:
        ans += int(game)

print("Answer A:", ans)

# part b
ans = 0
max_cubes_per_game = find_max_cubes_per_color(input)
for game in max_cubes_per_game.keys():
    red, green, blue = max_cubes_per_game[game]
    ans += (red * green * blue)

print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
