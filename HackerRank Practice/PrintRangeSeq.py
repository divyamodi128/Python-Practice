from __future__ import print_function

n = int(input())

# For Python 2.7
#print "".join([str(i) for i in range(1, n + 1)])

print ("".join([i for i in range(1, n + 1)]))

# For Pyhton 3.0
for i in range(1, n + 1):
    print(i, end="")

# map()

print ("12{}".format(n))