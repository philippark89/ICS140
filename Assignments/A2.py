'''
Author Taeju Park
This program reads price and dicount then calculate the total price

Pseudo Code 
Read the price into price
Read the amound of discount into discount
Set total to price - discount
Print price, discount, and total

Sample Set 1:
Sample input: 25.5 20.5
Sample output: 25.5 20.5 5.0

Sample Set 2:
Sample input: 52.0 12.0
Sample output: 52.0 12.0 40.0
'''

price = float(input('Enter sale price: ')) # reads original price
discount = float(input('Enter discount: ')) # reads discount amount
total = price - discount # calculate the total price
print(price, discount, total) # print price, discount, and total
