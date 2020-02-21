'''
Author: Taeju Park

This program reads the work hours then determine is it over time worked or not and calculate the total payment.

Pseudo Code
Read the hours that user worked into hours_worked
If hours_worked is more than 80 then print 'Invalid input'
Otherwise if hours_worked is less than equal to 40 then
	read pay rates into pay_rate
	set total_pay = pay_rate * hours_worked
	print the hours_worked, pay_rate, and total_pay

	otherwise
	read pay rates into pay_rate
	read pay rates for overtime into pay_rate_overtime
	set overtime = hours_worked - 40
	set fulltime = 40
	set total_pay = (fulltime * pay_rate) + (overtime * pay_rate_overtime)
	print the first full time which 40, pay_rate, overtime, pay_rate_overtime, and total_pay

Data Set 1:

Sample Input
Enter hours worked: 35
Enter basic pay rate: 12.5

Sample Output
35 hours at $12.5 per hour; total pay $437.5

Data Set 2:
Enter hours worked: 80
Enter basic pay rate: 12.5
Enter overtime pay rate: 15

Sample Output
First 40 hours at $12.5 per hour and next 40 hours at $15.0 per hour; total pay $1100.0


'''

hours_worked = int(input('Enter hours worked: '))

if hours_worked > 80:
	print('Invalid input')
else:
	if hours_worked <= 40:
		pay_rate = float(input('Enter basic pay rate: '))
		total_pay = pay_rate * hours_worked
		print(str(hours_worked) + ' hours at $' + str(pay_rate) + ' per hour; total pay $' + str(total_pay))
	else:
		pay_rate = float(input('Enter basic pay rate: '))
		pay_rate_overtime = float(input('Enter overtime pay rate: '))
		overtime = hours_worked - 40
		fulltime = 40
		total_pay = (fulltime * pay_rate) + (overtime * pay_rate_overtime)
		print('First ' + str(fulltime) + ' hours at $' + str(pay_rate) + ' per hour and next '+ str(overtime) + ' hours at $' + str(pay_rate_overtime) + ' per hour; total pay $' + str(total_pay))