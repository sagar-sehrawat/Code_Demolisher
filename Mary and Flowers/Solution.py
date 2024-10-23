#!/usr/bin/env python3

## This is an Unstop Site chall

n_and_target = input().split()
num_flower_types = int(n_and_target[0])
target_flower_count = int(n_and_target[1])

flower_counts = list(map(int, input().split()))

solution_found = False

for outer_index in range(num_flower_types):
    for inner_index in range(outer_index + 1, num_flower_types): 
        flower_sum = flower_counts[outer_index] + flower_counts[inner_index]
      
        if flower_sum == target_flower_count:
            print(outer_index, inner_index)
            solution_found = True
            break
    if solution_found:
        break
