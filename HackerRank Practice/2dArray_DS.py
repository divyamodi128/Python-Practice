from __future__ import print_function

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

maxim = -99999
for arr_i in xrange(4):
    for arr_j in xrange(4):
        temp_sum = 0
        for i in xrange(3):
            for j in xrange(3):
                if not (i is 1 and (j is 0 or j is 2)):
                    temp_sum += arr[arr_i + i][arr_j + j]
                    print(arr[arr_i + i][arr_j + j], end=" ")
            print()
        print(temp_sum, end="\n\n")
        if maxim < temp_sum:
            maxim = temp_sum
print(maxim)

"""
Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4

"""