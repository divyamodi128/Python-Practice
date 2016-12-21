def merge_the_tools(s, k):
    for i in xrange(k):
        str = ''
        temp = s[k*i: k*i+k]
        for c in temp:
            if c not in str:
                str += c
        print str

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)