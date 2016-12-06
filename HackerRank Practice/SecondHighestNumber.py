n = int(input())

ls = map(int,raw_input().strip().split())[:n]

print ls                            # Simple list
print set(ls)                       # Converts it into set without duplication
print list(set(ls))                 # Sets need to be converted into lists
print sorted(list(set(ls)))         # Sorting ascending
print sorted(list(set(ls)))[-2]     # Second Last or second highest from the list

# This is same as followed
# z = max(ls)
# while max(ls) == z:
#     ls.remove(max(ls))
#
# print max(ls)

# nput (stdin)
#
# 5
# 2 3 6 6 5
#
# Your Output (stdout)
#
# 5
