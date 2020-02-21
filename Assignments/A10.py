'''
Author Taeju Park

This program reads the city names then contain to the list.
Compare the city name with the city list.
If the city is exist in the list, it prints the information
The program will prints depends on where the elements stored in list
i.e. if the city name stored on second of the list,
It will prints first, second, and third.
If the city name stored on first of the list,
It will prints first and second.
If the city name stored on last of the list,
It will prints the second from the last city and the last city.
Otherwise, it prints 'not found'

Pseudo Code
Create the function name get_schedule no parameter
	Read the number of cities into num_cities
	Set city_list to empty list
	Loop the list of num_cities
		Read city names into city
		Append the city names to list city_list
	Return the city_list

Create the function name print_info with two parameters, cities and city.
	If city in cities then
		Set index to index of city in list cities
		If index == 0 then
			print(city, 'followed by', cities[1])
		or if index == length of cities - 1 then
			print(city, 'preceded by', cities[index - 1])
		Otherwise
			print(city, 'preceded by', cities[index - 1], \
				'and followed by', cities[index + 1])
	Otherwise
		print(city, 'not found')

Create the function name main no parameters
	Set cities to get_schedule()
	Read city to search into ask

	Loop until ask is blank(hit enter)
		Call function print_info(cities, ask)
		Read city to search info ask

Call the function main()


Data Tests
---------------------------------------------------Test number 1
Number of cities - 5
City names - Ansan, Seoul, Busan, Mokpo, and Daegu
City - Seoul
Expected Output - Seoul preceded by Ansan and followed by Busan

---------------------------------------------------Test number 2
Number of cities - 3
City names - Seattle, Greenbay, and stPaul
City - Minneapolis
Expected Output - Minneapolis not found

---------------------------------------------------Test number 3
Number of cities - 5
City names - Melbourne, Sydney, Perth, Canbera, and GoldCoast
City - Melbourne
Expected Output - Melbourne followed by Sydney


'''

def get_schedule():
	num_cities = int(input('Enter the number of cities: '))
	city_list = []

	for i in range(num_cities):
		city = input('Enter next city: ')
		city_list.append(city)

	return city_list

def print_info(cities, city):
	if city in cities:
		index = cities.index(city)
		if index == 0:
			print(city, 'followed by', cities[1])
		elif index == len(cities) - 1:
			print(city, 'preceded by', cities[index - 1])
		else:
			print(city, 'preceded by', cities[index - 1], \
				'and followed by', cities[index + 1])
	else:
		print(city, 'not found')

def main():
	cities = get_schedule()
	ask = input('Enter city to search: ')

	while ask != '':
		print_info(cities, ask)
		ask = input('Enter city to search: ')

main()