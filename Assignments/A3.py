'''
Author Taeju Park

The program reads in the x and y coordinates of the end points of a straight line. It computes the slope of
the line and prints the coordinate values read in and the slope. The coordinates may have decimal points
in them.

Pseudo Code
Read the first x-coordinate into x1
Read the first y-coordinate into y1
Read the second x-coordinate into x2
Read the second y-coordinate into y2
Set slope to (y2 - y1) / (x2 - x1)
Print the slope

Sample set1:
Input: x1 = 2, y1 = 1.5, x2 = 3, y2 = 4
expected output for the above data,the slope is 2.5

Sample set2:
Input: x1 = 5, y1 = 4, x2 = 2, y2 = 1
expected output for the above data, the slope is 1.0

'''

x1 = float(input("Enter point 1's x-coordinate value: "))
y1 = float(input("Enter point 1's y-coordinate value: "))
x2 = float(input("Enter point 2's x-coordinate value: "))
y2 = float(input("Enter point 2's y-coordinate value: "))

slope = (y2 - y1) / (x2 - x1)

print('The slope is', slope)
