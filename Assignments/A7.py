'''
Author Taeju Park

This program reads amount of temperature, wind speed, and humidity. It calculates and prints average of temperature, highest wind speed, and current humidity from user inputs.

Pseudo Code.
Set temp_count to 0
Set temp_sums to 0
Read temperature into temperature
While temperature is not space input
	Set temp_int to integer of temperature
	Set temp_counter to temp_counter + 1
	Set temp_sums to temp_sums + temp_int
	Read temperature into temperature
If temp_sums is 0
	set temp_avg to 'No info on temperature'
otherwise 
	set temp_avg to integer of (temp_sums / temp_counter)

Set wind_max to 0
Read wind speed into integer of wind
While wind is not -1
	If wind_max is more than wind
		set wind_max to wind
	Read wind speed into integer of wind
If wind_max is 0
	set wind_max to 'No info on wind speed'

Set humidity_current to 0
Read current humidity into integer of humidity
While humidity is less than 101 and more than -1
	If humidity is less than 101 and more than -1
		Set humidity_current to humidity
	Read current humidity into integer of humidity
If humidity_current is 0
	Set humidity_current to 'No info on humidity'

Print 'Average temperature', temp_avg
Print 'Maximum wind speed', wind_max
Print 'Current humidity', humidity_current

Sample Sets

Input 1
Enter temperature: 10
Enter temperature: 20
Enter temperature: 30
Enter temperature: 
Enter wind speed: 10
Enter wind speed: 20
Enter wind speed: 30
Enter wind speed: -1
Enter current humidity (0-100): 40
Enter current humidity: 60
Enter current humidity: 70
Enter current humidity: 101

Expected Output for the above data
Average temperature 20
Maximum wind speed 30
Current humidity 70

Input 2
Enter temperature: 
Enter wind speed: 20
Enter wind speed: -1
Enter current humidity (0-100): 70
Enter current humidity: 105

Expected Output for the above data
Average temperature No info on temperature
Maximum wind speed 20
Current humidity 70

Input 3
Enter temperature: 20
Enter temperature: 
Enter wind speed: -1
Enter current humidity (0-100): 30
Enter current humidity: 50
Enter current humidity: 300

Expected Output for the above data
Average temperature 20
Maximum wind speed No info on wind speed
Current humidity 50

Input 4
Enter temperature: 30
Enter temperature: 40
Enter temperature: 50
Enter temperature: 
Enter wind speed: 20
Enter wind speed: 30
Enter wind speed: -1
Enter current humidity (0-100): 111

Expected Output for the above data
Average temperature 40
Maximum wind speed 30
Current humidity No info on humidity
'''

temp_counter = 0
temp_sums = 0
temperature = input("Enter temperature: ")

while temperature != '': # temperature loop
	temp_int = int(temperature)
	temp_counter += 1
	temp_sums += temp_int
	temperature = input("Enter temperature: ")

if temp_sums == 0:
	temp_avg = 'No info on temperature'
else:
	temp_avg = int(temp_sums / temp_counter)


wind_max = 0
wind = int(input("Enter wind speed: "))

while wind != -1: # wind loop
	if wind_max < wind:
		wind_max = wind
	wind = int(input("Enter wind speed: "))

if wind_max == 0:
	wind_max = 'No info on wind speed'

humidity_current = 0
humidity = int(input("Enter current humidity (0-100): "))

while humidity < 101 and humidity > -1:
	if humidity < 101 and humidity > -1:
		humidity_current = humidity
	humidity = int(input("Enter current humidity: "))

if humidity_current == 0:
	humidity_current = 'No info on humidity'

print('Average temperature', temp_avg)
print('Maximum wind speed', wind_max)
print('Current humidity', humidity_current)