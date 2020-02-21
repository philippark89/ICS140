even_count = 0
odd_count = 0

temp = input('Enter an integer: ')

while temp != "":
	num = int(temp)

	if num % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	
	temp = input('Enter an integer: ')


print('Number of even integer:', even_count)
print('Number of odd integer:', odd_count)
