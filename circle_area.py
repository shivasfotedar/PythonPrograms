import math

def area_of_circle(radius):
    return math.pi*radius**2

radius = float(input('Enter thr value of radius:'))
print('Area of circle with radius %.2f is %.2f' %(radius,area_of_circle(radius)))