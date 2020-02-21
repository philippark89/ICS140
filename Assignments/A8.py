'''
Author Taeju Park

This program print big size of character with filled characters.
The size will be depends on the user input height and width

Pseudo Code
Set check_hiehgt to True
Set check_width to True
Read the width of the character into width
While check_width is False
	If width % 4 is 0 then
		set check_width to False
	Otherwise
		Read the width of the character into width

Read the height of the character into heigth
While check_height is False
	If height % 8 is 0 then
		set check_height to False
	Otherwise
		Read the height of the character into height

For row in range of (height - (height // 4) // 2)
	For col in range of (width // 4)
		print('H', end='')
	For col in range of (width // 2)
		print('', end='')
	For col in range of (width // 4)
		print('H', end='')
	print()

For row in range of (height // 4)
	For col in range of (width)
		print('H', end='')
	print()

For row in range of (height - (height // 4) // 2)
	For col in range of (width // 4)
		print('H', end='')
	For col in range of (width // 2)
		print('', end='')
	For col in range of (width // 4)
		print('H', end='')
	print()

Sample Set 1:
Input:
Enter width: (divisible by 4): 4
Enter height: (divisible by 8): 8

Output:
H  H
H  H
H  H
HHHH
HHHH
H  H
H  H
H  H

Sample Set 2:
Input:
Enter width: (divisible by 4): 16
Enter height: (divisible by 8): 24

Output:
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
HHHH        HHHH
'''
check_height = True
check_width = True

width = int(input('Enter width: (divisible by 4): '))

while check_width:
	if width % 4 == 0:
		check_width = False
	else:
		width = int(input('The width should be divisible\
					by 4: Please re-enter: '))

height = int(input('Enter height: (divisible by 8): '))

while check_height:
	if height % 8 == 0:
		check_height = False
	else:
		height = int(input('The height should be divisible\
					 by 8: Please re-enter: '))

# above vertical bars
for row in range((height - (height // 4)) // 2):
	for col in range(width // 4):
		print('H', end='')

	for col in range(width // 2):
		print(' ', end='')

	for col in range(width // 4):
		print('H', end='')
	print()

# center bar
for row in range(height // 4):
	for col in range(width):
		print('H', end='')
	print()

# bottom vertical bars
for row in range((height - (height // 4)) // 2):
	for col in range(width // 4):
		print('H', end='')

	for col in range(width // 2):
		print(' ', end='')

	for col in range(width // 4):
		print('H', end='')
	print()
