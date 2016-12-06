#import sys

N = int(raw_input())
# Case #1

# if N % 2 != 0:
#     print "Weird"
# elif N >= 2 & N <= 5:
#     print "Not Weird"
# elif N >= 6 & N <= 20:
#     print "Weird"
# else:
#     print "Not Weird"

# Case #2

# if N % 2 != 0 or N in range(6, 20):
#     print "Weird"
# else:
#     print "Not Weird"

# Case #3
if N % 2 != 0 or N in range(6, 21):
    print "Weird"
else:
    print "Not Weird"