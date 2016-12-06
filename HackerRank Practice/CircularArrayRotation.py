import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
for a0 in xrange(q):
    m = int(raw_input().strip()) - k % n
    print "m =", m
    #if m <= 0:
     #   m = q-1
    print a[m]


"""
3 2 5
1 2 3
0
1
2
3
4
"""