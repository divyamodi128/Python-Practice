# from __future__ import print_function

x, y, z, n = (int(input()) for _ in range(4))
# This is Equivalent to
# x, y, z, n = int(input()), int(input()), int(input()), int(input())

print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])
# This is Equivalent to
# list1 = []
# for a in range(0, x + 1):
#     for b in range(0, y + 1):
#         for c in range(0, z + 1):
#             if a + b + c != n:
#                 list1.append([a, b, c])
#
# print list1

# Input (stdin)
#
# 2
# 2
# 2
# 2
#
# Your Output (stdout)
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
