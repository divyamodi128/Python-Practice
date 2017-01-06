from collections import namedtuple
"""
Short Method:
"""
n=int(input())
stdlt = namedtuple('stdlt', raw_input().split())
print sum([int(stdlt(*raw_input().split()).MARKS) for _ in range(n)])//n


"""
Long Method:

n,marks=int(input()),0
stdlt = namedtuple('stdlt', ', '.join(raw_input().split()))
for _ in range(n):
    ls = raw_input().split()
    xyz = stdlt(*ls)
    marks += int(xyz.MARKS)
print(marks/n)
"""

"""
Example how to use 'collections.namedtuple'

Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print xyz.Class
Y
"""