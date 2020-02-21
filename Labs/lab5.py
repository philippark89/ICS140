mass = float(input('Enter mass in kilogram: '))
weight = mass * 9.8

if weight > 980:
    print('The object is too heavy to be lifted')
else:
    print('The object can be lifted')
    if weight <= 98:
        print('The object is quite light')

        
