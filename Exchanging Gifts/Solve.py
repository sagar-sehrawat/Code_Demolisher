#!/usr/bin/env python3

## Unstop site

from collections import Counter

temp_inp = input().split()

fam_mem_gift_no = list(map(int, temp_inp))
gift_exch = fam_mem_gift_no[1]

younger_list = []

for i in range(gift_exch):
    temp_exc = input().split()
    exhcnages = list(map(int, temp_exc))
    
    younger = exhcnages[1]  
    younger_list.append(younger)

count = Counter(younger_list)
most_common = count.most_common(1)  
print(most_common[0][0])
