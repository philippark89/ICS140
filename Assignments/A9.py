'''
Author Taeju Park

The program generates the two numbers and the operation then
compare with user's answer determine the answer is correct or not.
Also, the program asks to play again or not after every attemps.

Pseudo Code
import random for using randint
Create the function name new_number no parameter
	Return the random integer between 1 and 100

Create the function name get_operation no parameter
	Set pick to random interger between 1 and 4
	Set operation to empty string
	If pick is 1 then
		Set operation to '+'
	Elif pick is 2 then
		Set operation to '-'
	Elif pick is 3 then
		Set operation to '*'
	Elif pick is 4 then
		Set operation to '//'

	The function returns operation

Create the function name check with parameter called
number1, number2, operation, and guess
	Set correct_answer to 0
	If operation is '+' then
		Set correct_answer to number1 + number2
	Elif operation is '-' then
		Set correct_answer to number1 - number2
	Elif operation is '*' then
		Set correct_answer to number1 * number2
	Elif operation is '//' then
		Set correct_answer to number1 // number2

	If correct_answer is guess then
		the function returns True and correct_answer
	Else
		the function returns False and correct_answer

Create the function name start no parameter
	Set end to 'n'
	While end is not 'y'
		Set num1 to new_number()
		Set num2 to new_number()
		Set operation to get_operation()
		print ('What is', num1, operation, num2, '? ', end='')
		Read the guessing number into guess
		Call the function check
		If checking[0] is True then
			print('You answered correctly')
		Else
			print('The correct answer is', checking[1])

		Read yes or no to play again into end

Call the funtion start()


Data Test
-------------------------------------------------
/ 	input 		/ 	Expected Output				/
-------------------------------------------------
/				/	What is 47 + 52 ?			/
/	99			/	You answered correctly		/
/				/	End? y or n:				/ 
/	n			/								/	
/				/	What is 19 - 10 ?			/
/	10			/	The correct answer is 9		/
/				/	End? y or n:				/ 
/	n			/								/
/				/	What is 29 * 11 ?			/
/	155			/	The correct answer is 319	/
/				/	End? y or n:				/
/	n 			/								/
/				/	What is 47 + 52 ?			/
/	99			/	You answered correctly		/
/				/	End? y or n:				/
/	n 			/								/
/				/	What is 81 // 14 ?			/
/	4			/	The correct answer is 5		/
/				/	End? y or n:				/
/	n 			/								/
/				/	What is 89 - 11 ?			/
/	78			/	You answered correctly		/
/				/	End? y or n:				/
/	n 			/								/
/				/	What is 35 + 15 ?			/
/	60			/	The correct answer is 50	/
/				/	End? y or n:				/
/	y 			/								/
-------------------------------------------------

'''

import random

def new_number():
	return random.randint(1, 100)

def get_operation():
	pick = random.randint(1, 4)
	operation = ''

	if pick == 1:
		operation = '+'
	elif pick == 2:
		operation = '-'
	elif pick == 3:
		operation = '*'
	elif pick == 4:
		operation = '//'

	return operation

def check(number1, number2, operation, guess):
	correct_answer = 0
	if operation == '+':
		correct_answer = number1 + number2
	elif operation == '-':
		correct_answer = number1 - number2
	elif operation == '*':
		correct_answer = number1 * number2
	elif operation == '//':
		correct_answer = number1 // number2

	if correct_answer == guess:
		return True, correct_answer
	else:
		return False, correct_answer

def start():
	end = 'n'
	while end != 'y':
		num1 = new_number()
		num2 = new_number()
		operation = get_operation()
		print ('What is', num1, operation, num2, '? ', end='')
		guess = int(input())
		checking = check(num1, num2, operation, guess)

		if checking[0] == True:
			print('You answered correctly')
		else:
			print('The correct answer is', checking[1])

		end = input('End? y or n: ')

start()