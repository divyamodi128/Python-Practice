string1 = raw_input()
string2 = raw_input()

times = 0
for i in range(0, len(string1)):
    if string1[i:i + len(string2)] == string2:
        times += 1

print times

# Can\'t be represented by
# print (times for i in range(0, len(string1)): if string1[i:i + len(string2)] == string2: times += 1)

# Sample Input
#
# ABCDCDC
# CDC
#
# Sample Output
#
# 2
#
# Concept