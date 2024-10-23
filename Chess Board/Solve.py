#!/usr/bin/env python3
# This is an Unstop site chall

position = input()
y_axis = int(position[1])

color = 'White'

if position[0] == 'a' or position[0] == 'c' or position[0] == 'e' or position[0] == 'g':
	if y_axis%2==0:
		color = 'White'
	else:
		color = 'Black'
elif position[0] =='b' or position[0] =='d' or position[0] =='f' or position[0] =='h':
	if y_axis%2==0:
		color = 'Black'
	else:
		color = 'White'
print(color)


