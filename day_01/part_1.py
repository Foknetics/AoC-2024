with open('input.txt') as f:
    lines = f.read().splitlines()

left_location_ids = []
right_location_ids = []
for line in lines:
    left, right = line.split('   ')
    left_location_ids.append(int(left))
    right_location_ids.append(int(right))

left_location_ids.sort()
right_location_ids.sort()

total_distance_delta = 0
for index in range(len(left_location_ids)):
    total_distance_delta += abs(left_location_ids[index] - right_location_ids[index])

print(f'The total distance between the the lists is: {total_distance_delta}')
