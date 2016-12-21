a = raw_input()
print a
res = {}
for ch in a:
    if ch in res.keys():
        res[ch] += 1
    else:
        res[ch] = 1
# print sorted(res)
for w in sorted(res, key=res.get, reverse=True)[:3]:
    print w, res[w]

"""
Sample Input

aabbbccde

Sample Output

b 3
a 2
c 2

Sample Input 2
qwertyuiopasdfghjklzxcvbnm
a 1
b 1
c 1
"""