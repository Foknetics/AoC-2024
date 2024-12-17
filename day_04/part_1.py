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
    word_search = f.read().splitlines()

matches = 0


def diagonal_text(word_search, row, col, left_to_right=True):
    if left_to_right is False:
        col = len(word_search[0]) - col - 1

    text = ''
    in_bounds = True
    while in_bounds:
        if col < 0:
            break

        try:
            text += word_search[row][col]
        except IndexError:
            in_bounds = False

        row += 1
        if left_to_right:
            col += 1
        else:
            col -= 1

    return text


# Horizontal
for line in word_search:
    logger.info('Processing horizontal line: %s', line)
    logger.info('New matches: %s', len(re.findall(r'(?=(XMAS|SAMX))', line)))
    matches += len(re.findall(r'(?=(XMAS|SAMX))', line))

# Vertical
for column in range(len(word_search[0])):
    column_text = ''.join([word_search[row][column] for row in range(len(word_search))])
    logger.info('Processing vertical line: %s', column_text)
    logger.info('New matches: %s', len(re.findall(r'(?=(XMAS|SAMX))', column_text)))
    matches += len(re.findall(r'(?=(XMAS|SAMX))', column_text))

# Diagonals
top_row = [(0, col) for col in range(len(word_search[0]))]
side_col = [(row, 0) for row in range(1, len(word_search))]
for (row, column) in top_row + side_col:
    # Left to Right
    logger.info(
        'Processing L2R diagonal from %s, %s line: %s',
        row, column, diagonal_text(word_search, row, column)
    )
    logger.info(
        'New matches: %s',
        len(re.findall(r'(?=(XMAS|SAMX))', diagonal_text(word_search, row, column)))
    )
    matches += len(re.findall(r'(?=(XMAS|SAMX))', diagonal_text(word_search, row, column)))

    # Right to Left
    logger.info(
        'Processing R2L diagonal from %s, %s line: %s',
        row, column, diagonal_text(word_search, row, column, False)
    )
    logger.info(
        'New matches: %s',
        len(re.findall(r'(?=(XMAS|SAMX))', diagonal_text(word_search, row, column, False)))
    )
    matches += len(re.findall(r'(?=(XMAS|SAMX))', diagonal_text(word_search, row, column, False)))


print(f'XMAS appears {matches} times in the word search')
