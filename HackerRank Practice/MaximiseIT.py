"""K, M = [int(x) for x in raw_input().split(" ")]
arrayN = []
for _i_ in range(K):
    arrayN.append([int(x) for x in raw_input().split(" ")][1:])

from itertools import product
possible_combination = list(product(*arrayN))
print possible_combination

def func(nums):
    return sum(x*x for x in nums) % M

print(max(list(map(func, possible_combination))))
"""
k, m = [int(x) for x in raw_input().split(" ")]
l1 = [map(int, raw_input().strip().split()) for _ in xrange(int(k))]
print l1

def my_sum(list1):
    return sum(int(i) * int(i) for i in list1) % m
    print "l2:", l2
    return (l2 * l2) % m

# sum1 = 0
# for list1 in l1:
#     sum1 += max(my_sum(list1))
# print sum1
print "temp zip", zip(l1[0], l1[1], l1[2])
print "zip", zip(l for l in l1)
print(max(list(map(my_sum, zip(l for l in l1)))))
print sum([my_sum(list2) for list2 in l1]) % m
    # print my_sum(list)
"""
def f(num):
    return int(num) % m

l1 = set([max(map(f, raw_input().strip().split())) for _ in xrange(k)])
print sum(i * i for i in l1) % m
"""

"""
Input:
6 767
2 488512261 423332742
2 625040505 443232774
1 4553600
4 92134264 617699202 124100179 337650738
2 778493847 932097163
5 489894997 496724555 693361712 935903331 518538304

Output:
763
"""