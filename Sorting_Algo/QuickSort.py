def quicksort(array):
    less, greater = [], []
    if len(array) < 2:
        return array
    # select and remove a pivot value pivot from array
    pivot = array.pop()
    for x in array:
        if x < pivot + 1:
            # then append x to less
            less.append(x)
        else:
            # append x to greater
            greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)


lst = [7, 8, 3, 5, 6, 7, 1, 5, 6, 9, 2]
print(quicksort(lst))
lst1 = [26, 56, 12, 45, 95, 63, 57, 85, 64, 60]
print(quicksort(lst1))

print(quicksort([26, 56, 12, 45, 95, 63, 57, 85, 64, 57]))
