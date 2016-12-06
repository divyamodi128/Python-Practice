import numpy
"""
my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
"""
n = map(int, raw_input().strip().split(" "))
list = [[int(i) for i in raw_input().strip().split()]]
print list
my_array = numpy.array([map(int, raw_input().strip().split(" ")), map(int, raw_input().strip().split(" "))])
print my_array
# print numpy.mean(my_array, axis=1)
# print numpy.var(my_array, axis=0)
# print numpy.std(my_array)
"""
Output Format

First, print the mean.
Second, print the var.
Third, print the std.

Sample Input

2 2
1 2
3 4

Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875

"""