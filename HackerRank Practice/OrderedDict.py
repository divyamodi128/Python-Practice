from collections import OrderedDict, Counter
dict = OrderedDict()
for _ in range(int(input())):
    name,_,price=raw_input().rpartition(' ')
    # ls = raw_input().split()
    dict[name] = dict.get(name,0) + int(price)

print('\n'.join(key+' '+str(value) for key,value in dict.items()))

"""
Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

"""