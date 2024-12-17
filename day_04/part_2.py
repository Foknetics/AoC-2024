def cross_check(word_search, x, y):
    matches = 0
    try:
        top_left = word_search[y-1][x-1]
        top_right = word_search[y-1][x+1]
        center = word_search[y][x]
        bottom_left = word_search[y+1][x-1]
        bottom_right = word_search[y+1][x+1]

        # M.S
        # .A.
        # M.S
        if (center == 'A' and top_left == 'M' and top_right == 'S'
                and bottom_left == 'M' and bottom_right == 'S'):
            matches += 1

        # S.M
        # .A.
        # S.M
        if (center == 'A' and top_left == 'S' and top_right == 'M'
                and bottom_left == 'S' and bottom_right == 'M'):
            matches += 1

        # S.S
        # .A.
        # M.M
        if (center == 'A' and top_left == 'S' and top_right == 'S'
                and bottom_left == 'M' and bottom_right == 'M'):
            matches += 1

        # M.M
        # .A.
        # S.S
        if (center == 'A' and top_left == 'M' and top_right == 'M'
                and bottom_left == 'S' and bottom_right == 'S'):
            matches += 1
    except IndexError:
        pass
    return matches


with open('input.txt') as f:
    word_search = f.read().splitlines()

matches = 0
for x in range(1, len(word_search)-1):
    for y in range(1, len(word_search)-1):
        matches += cross_check(word_search, x, y)

print(f'Crossed MAS appears {matches} times in the word search')
