"""n, q = map(int, raw_input().strip().split(" "))
last_ans, seq1, seq2 = 0, [], []
for _ in xrange(q):
    i, x, y = map(int, raw_input().strip().split(" "))
    seq = ((x ^ last_ans) % n)
    if i is 1:
        if seq == 1:
            seq1.append(y)
        else:
            seq2.append(y)
    else:
        if seq == 1:
            last_ans = seq1[y % len(seq1)]
            print last_ans
        else:
            last_ans = seq2[y % len(seq2)]
            print last_ans
"""

import sys

inp_arr = [int(arr_temp) for arr_temp in raw_input().strip().split(' ')]
N=inp_arr[0]
iter=inp_arr[1]
lastAns=0

seq_list = [[] for _ in range(N)]

for x in range(0,iter):
    iter_arr = [int(arr_temp) for arr_temp in raw_input().strip().split(' ')]
    position = (iter_arr[1] ^ lastAns) % N
    if iter_arr[0] == 1:
        seq_list[position].append(iter_arr[2])
    elif iter_arr[0] == 2:
        lastAns = (seq_list[position][iter_arr[2] % len(seq_list[position])] )
        print(lastAns)