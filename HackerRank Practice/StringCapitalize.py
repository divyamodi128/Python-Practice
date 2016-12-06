from __future__ import print_function

n = raw_input().split()
for i in range(0, n.__len__()):
    a = n[i]
    print(a.capitalize(), end=" ")

print([i.capitalize() for i in n])