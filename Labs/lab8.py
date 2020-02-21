top_height = 3
top_width = 9
bottom_height = 6
bottom_width = 3

for row in range(top_height): #3
	for column in range(top_width): #9
		print("T", end='')
	print()

for row in range(bottom_height): #6
	print('   ', end='')
	for column in range(bottom_width): #3
		print('T', end='')
	print()