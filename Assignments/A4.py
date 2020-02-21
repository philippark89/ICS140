'''
Author: Taeju Park

This program reads the menus from user then calculate and print receipt about total cost and change.

Pseudo Code
Create a Sandwich, Side dish, and Drink mapping
Create a lists of Sandwich, Side dish, and Drink
Read Sandwich menu from the list of Sandwich into sandwich
Read Side dish menu from the list of Side dish into side_dish
Read Drink menu from the list of Drink into drink
Read cash paid into cash_paid
Set total to sandwich + side_dish + drink
Set change to cash_paid - total
Print prices for sandwich, side dish, drink, total, cash paid, and change as receipt.

Data Set 1:

Sample Input
veggie sandwich
salad
bottled water
Total is $4.5 Enter cash paid 5.0

Expected Output for the above data

Receipt:
veggie sandwich $2.0
salad $1.5
bottled water $1.0
Total $4.5
Cash tendered $5.0
Change $0.5

Data Set 2:

Sample Input
chicken
fries
juice
Total is $6.0 Enter cash paid 10.0

Expected Output for the above data

Receipt:
chicken sandwich $3.5
fries $0.5
juice $2.0
Total $6.0
Cash tendered $10.0
Change $4.0

'''

dict_sandwich = {'beef': 3.0, 'chicken': 3.5, 'cheese': 1.5, 'veggie': 2.0}
dict_side_dish = {'salad': 1.5, 'soup': 2.0, 'garlic bread': 1.0, 'fries': 0.5}
dict_drink = {'juice': 2.0, 'soda': 1.5, 'bottled water': 1.0}

list_sandwich = ['beef', 'chicken', 'cheese', 'veggie']
list_side_dish = ['salad', 'soup', 'garlic bread', 'fries']
list_drink = ['juice', 'soda', 'bottled water']

print('Choose a sandwich from: ', list_sandwich)
sandwich = input()
print('Choose a side dish from: ', list_side_dish)
side_dish = input()
print('Choose a drink from: ', list_drink)
drink = input()

cash_paid = float(input('Total is $' + str(dict_sandwich[sandwich] + dict_side_dish[side_dish] + dict_drink[drink]) + ' Enter cash paid '))

total_price = dict_sandwich[sandwich] + dict_side_dish[side_dish] + dict_drink[drink]
change = cash_paid - total_price

print('Receipt:\n' + sandwich + ' sandwich $' + str(dict_sandwich[sandwich]) + '\n' + side_dish + ' $' + str(dict_side_dish[side_dish]) + '\n' + drink + ' $' + str(dict_drink[drink]) + '\n' + 'Total $' + str(total_price) + '\nCash tendered $' + str(cash_paid) + '\nChange $' + str(change))