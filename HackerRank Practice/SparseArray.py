array = [raw_input() for _ in xrange(int(input()))]
for _ in xrange(int(input())):
    temp_str = raw_input()
    print sum([1 for arr in array if temp_str == arr])

"""
Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output

2
1
0

"""