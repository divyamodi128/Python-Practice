def findrepeats(str):
    for i in range(len(str)):
        count = 0
        for j in range(i,len(str)):
            print(str[i], str[j])
            if str[i] == str[j]:
                count += 1
        if count >= 3:
            print(str[i] * count)
            str = str.replace(str[i] * count, '')
    print('Final String', str)

import re
def findrepeats1(str):
    setstr = set(str)
    for s in setstr:
        l = len(re.findall(s, str))
        if l >= 3 and re.findall(s * l, str):
            print('Removing:', s * l)
            str = str.replace(s * l, '')
    return str


print(findrepeats('abbbccdeeeef'))
print(findrepeats1('abbcccddeeeefdd'))

"""
Input 1 : 'abbbccdeeeef'
Output 1 : 'acdf'

Input 2 : 'aaabcdefffffgggh'
Output 2 : 'bcdeh'
"""
