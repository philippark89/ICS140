'''
Author: Taeju Park

This is the calculator do add, subtract, multiply, divide, and square from depends on what user input. All the result will show with integer and division cannot be by 0

Pseudo Code
Print the commands list.
Read the commands such as a, s, m, d, and q into command.
If command is a then read the first number and second number, then print the sum of two numbers.
Or command is s then read the first number and second number, then print the difference of two numbers.
Or command is m then read the first number and second number, then print the product of two numbers.
Or command is d then read the first number and second number.
	if the second number is not 0 then print quotient of first and second number
	otherwise print Divisor cannot be 0
Or command is q then read the first number, then print the square of the first number.

Sample Input 1:
Enter command: a
Enter the first number: 15
Enter the second number: 20

Expected Output for the above data
The sum is 35

Sample Input 2:
Enter command: s
Enter the first number: 15
Enter the second number: 10

Expected Output for the above data
The difference is 5

Sample Input 3:
Enter command: m
Enter the first number: 5
Enter the second number: 12

Expected Output for the above data
The product is 60

Sample Input 4:
Enter command: d
Enter the first number: 12
Enter the second number: 5

Expected Output for the above data
The quotient is 2

Sample Input 5:
Enter command: d
Enter the first number: 12
Enter the second number: 0

Expected Output for the above data
Divisor cannot be 0

Sample Input 6:
Enter command: q
Enter the number to be squared: 14

Expected Output for the above data
The square is 196
'''

print('This is a simple calculator that supports \n\
 addition, subtraction, multiplication, diviision, and square\n\
Enter:\n\
 a to add,\n\
 s to subtract,\n\
 m to multiply,\n\
 d to divide,\n\
 q to square')

command = input('Enter command: ')

if command == 'a':
	first_num = int(input('Enter the first number: '))
	second_num = int(input('Enter the second number: '))
	print('The sum is ' + str(first_num + second_num))
elif command == 's':
	first_num = int(input('Enter the first number: '))
	second_num = int(input('Enter the second number: '))
	print('The difference is ' + str(first_num - second_num))
elif command == 'm':
	first_num = int(input('Enter the first number: '))
	second_num = int(input('Enter the second number: '))
	print('The product is ' + str(first_num * second_num))
elif command == 'd':
	first_num = int(input('Enter the first number: '))
	second_num = int(input('Enter the second number: '))
	if second_num != 0:
		print('The quotient is ' + str(first_num // second_num))
	else:
		print('Divisor cannot be 0')
elif command == 'q':
	first_num = int(input('Enter the number to be squared: '))
	print('The square is ' + str(first_num ** 2))
else:
	print('Invalid choice')