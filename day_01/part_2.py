with open('input.txt') as f:
    lines = f.read().splitlines()

left_location_ids = []
right_location_ids = []
for line in lines:
    left, right = line.split('   ')
    left_location_ids.append(int(left))
    right_location_ids.append(int(right))

similarity_score = 0
for index in range(len(left_location_ids)):
    similarity_score += left_location_ids[index] * \
                        right_location_ids.count(left_location_ids[index])

print(f'The similarity score between the lists is: {similarity_score}')
