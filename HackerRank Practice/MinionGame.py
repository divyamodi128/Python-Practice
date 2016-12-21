def minion_game(s):
    stuartcnt, kevincnt, ln = 0, 0,len(s)
    vowels = 'AEIOU'
    for i in xrange(ln):
        if s[i] in vowels:
            kevincnt += (ln - i)
        else:
            stuartcnt += (ln - i)
    # print "kevincnt:", kevincnt, "stuartcnt", stuartcnt

    if kevincnt > stuartcnt:
        print "Kevin", kevincnt
    elif stuartcnt > kevincnt:
        print "Stuart", stuartcnt
    else:
        print "Draw"


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
