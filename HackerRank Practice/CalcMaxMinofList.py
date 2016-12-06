#!/bin/python

import sys


#a,b,c,d,e = raw_input().strip().split(' ')
#a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
list = map(int,raw_input().strip().split(' '))
sum = sum(list)
print sum-max(list), sum-min(list)