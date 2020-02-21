def print_block(row, column, character):
	for row in range(row):
		for col in range(column):
			print(character, end='')
		print()

def print_E(width, height):
	row_long = width // 4
	col_long = height // 2
	row_short = width // 4
	col_short = height // 5

	print_block(row_long, col_long, 'E')
	print_block(row_short, col_short, 'E')
	print_block(row_long, col_long, 'E')
	print_block(row_short, col_short, 'E')
	print_block(row_long, col_long, 'E')


def print_L(width, height):
	top = height // 4
	bottom = width // 3
	
	print_block(width, top, 'L')
	print_block(bottom, height, 'L')


