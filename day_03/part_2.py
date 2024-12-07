import logging
import os
import re

if 'LOG_LEVEL' in os.environ:
    numeric_level = getattr(logging, os.environ['LOG_LEVEL'].upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {os.environ["LOG_LEVEL"]}')
    logging.basicConfig(level=numeric_level)
else:
    logging.basicConfig()

logger = logging.getLogger(__name__)


with open('input.txt') as f:
    corrupted_memory = f.read()

multiplication_totals = []
dos = re.finditer(r'do\(\)', corrupted_memory)
do_locations = [0]
for do in dos:
    do_locations.append(do.end())
logger.info('Locations of dos(): %s', do_locations)

dont_locations = []
donts = re.finditer(r'don\'t\(\)', corrupted_memory)
for dont in donts:
    dont_locations.append(dont.end())
logger.info('Locations of don\'ts(): %s', dont_locations)

multiplications = re.finditer(r'mul\((\d+),(\d+)\)', corrupted_memory)
for mul in multiplications:
    mul_loc = mul.start()
    logger.info('Testing %s at location: %s', mul.group(0), mul_loc)

    try:
        closest_do = [loc for loc in do_locations if loc <= mul_loc][-1]
    except IndexError:
        closest_do = -1

    try:
        closest_dont = [loc for loc in dont_locations if loc <= mul_loc][-1]
    except IndexError:
        closest_dont = -1

    logger.info('Closest do: %s, closest don\'t: %s', closest_do, closest_dont)

    if closest_do > closest_dont:
        logger.info('Adding to total %s*%s', mul.group(1), mul.group(2))
        multiplication_totals.append(int(mul.group(1))*int(mul.group(2)))

print(f'Sum of the multiplications is {sum(multiplication_totals)}')
