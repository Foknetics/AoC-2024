import re

with open('input.txt') as f:
    corrupted_memory = f.read().splitlines()

multiplication_totals = []
for line in corrupted_memory:
    matches = re.findall(r'mul\((\d+),(\d+)\)', line)
    multiplication_totals += [int(match[0])*int(match[1]) for match in matches]

print(f'Sum of the multiplications is {sum(multiplication_totals)}')
