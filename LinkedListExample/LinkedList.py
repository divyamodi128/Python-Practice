class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None;


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0


    def insertStart(self, data):

        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode


    def size1(self):
        return self.size


    def size2(self):

        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size


    def insertEnd(self, data):

        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode


    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print actualNode.data
            actualNode = actualNode.nextNode


    def removeNode(self, data):

        if self.head is None:
            return

        self.size -= 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode
        else:
            previousNode.nextNode = currentNode.nextNode


linkedlist = LinkedList()  # Instantiate LinkedList

linkedlist.insertStart(50)
linkedlist.insertStart(62)
linkedlist.insertStart(41)
linkedlist.insertEnd(82)

linkedlist.traverseList()

print "Size is", linkedlist.size1()
