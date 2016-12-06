n = int(input())
#ls = map(str,int,raw_input().strip().split())[:n]

ls = [[raw_input(), float(input())] for _ in range(0, n)]
print ls

# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([raw_input(), float(input())])
# print marksheet

print [marks for name, marks in ls]             # Didn't understand how this get only number or index[1] for each inner list
print set([marks for name, marks in ls])        # Removes duplications
print list(set([marks for name, marks in ls]))  # Type Casting to lists
print sorted(list(set([marks for name, marks in ls])))  # Sorts list in ascending order

secondlow = sorted(list(set([marks for name, marks in ls])))[1]     # Stores Second Lowest i.e. value of index[1]
print('\n'.join([a for a,b in sorted(ls) if b == secondlow]))

# z = int(map(min,ls))
# print z
# while min(ls[1]) == z:
#     print min(ls[:1]), "This will be removed from the List"
#     ls.remove(min(ls[:1]))
#
# print ls
# z = min(ls[1])
# print z
# while min(ls[1]) == z:
#     print min(ls[:1])
#     ls.remove(min(ls[:1]))
#
# print ls

# Sample Input
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
#
# Sample Output
#
# Berry
# Harry
