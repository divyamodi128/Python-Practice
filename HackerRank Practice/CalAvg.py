ls, name = [raw_input().strip().split() for _ in range(input())], raw_input()
# name = raw_input()

res = [(sum(map(float, i[1:])) / len(i[1:])) for i in ls if name in i]
print "%.2f" % res[0]
"""
for i in ls:
    if name in i:
        print "%.2f" % (sum(map(float, i[1:])) / len(i[1:]))
"""

        # for x in range(1,ls[i].__len__()):
        #     # print ls[i][x]
        #     count += 1
        #     s += float(str(ls[i][x]))
# print "%.2f" % round(s / count,2)


# n = int(input())
# ls = []
# for i in range(n):
#     temp = raw_input().strip().split()
#     ls.append([temp[0],map(int, temp[1:])])

"""
    This is an Comment
Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output

56.00

Explanation

Marks for Malika {52, 56, 60} are whose average is (52 + 56 + 60)/3 = 56"""