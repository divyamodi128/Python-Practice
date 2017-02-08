class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def print_list(head):
    if head:
        print(head.data)
        print_list(head.next)

for _ in range(int(input())):
    if int(input()):
        for i in list(map(int,input().split())):
            print_list(Node(i))


"""
Sample Input:
5
0
2
1 2
4
2 1 4 5
3
34 45 56
5
1 2 3 4 5

Sample Output:
1
2
2
1
4
5
34
45
56
1
2
3
4
5
"""