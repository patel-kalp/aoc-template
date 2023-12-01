#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
ans = 0
for line in input:
    digits = [char for char in line if char.isdigit()]
    if len(digits) >= 2:
        two_digit_number = int(digits[0] + digits[-1])
        ans += two_digit_number
    else:
        ans += int(digits[0] + digits[0])

print("Answer A:", ans)

# part b
ans = 0

spelled_out_digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

for line in input:
    first_digit = None
    last_digit = None

    for b in range(1, len(line)+1):
        for a in range(len(line)):
            word = line[a:b]
            num = None
            # print(word)
            if word.isdigit():
                num = word
            else:
                if word in spelled_out_digits.keys():
                    num = spelled_out_digits[word]
            
            if num is not None:
                if first_digit is None:
                    first_digit = num
                last_digit = num

    ans += int(first_digit[-1] + last_digit[-1])

print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
