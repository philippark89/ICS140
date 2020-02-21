print('This program reads in the length and width of a rectangle\nIt then prints the area and perimeter of the rectangle.')
length = float(input('Enter length: '))
width = float(input('Enter width: ' ))
area = length * width
perimeter = 2 * (length + width)

print('length', length, 'width', width, 'area', area,
      'perimeter', perimeter)
