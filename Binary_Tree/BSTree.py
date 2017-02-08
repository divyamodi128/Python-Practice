from Node import Node


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("Preorder Traversal:")
        self.root.preorder()

    def postorder(self):
        print("PostOrder Traersal:")
        self.root.postorder()

    def inorder(self):
        print("InOrder Traversal:")
        self.root.inorder()

    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # data is in root node
        elif self.root.data == data:
            if self.root.leftchild is None and self.root.rightchild is None:
                self.root = None
            elif self.root.leftchild and self.root.rightchild is None:
                self.root = self.root.leftchild
            elif self.root.leftchild is None and self.root.rightchild:
                self.root = self.root.rightchild
            elif self.root.leftchild and self.root.rightchild:
                delNodeParent = self.root
                delNode = self.root.rightchild
                while delNode.leftchild:
                    delNodeParent = delNode
                    delNode = delNode.leftchild

                self.root.data = delNode.data
                if delNode.rightchild:
                    if delNodeParent.data > delNode.data:
                        delNodeParent.leftchild = delNode.rightchild
                    elif delNodeParent.data < delNode.data:
                        delNodeParent.rightchild = delNode.rightchild
                else:
                    if delNode.data < delNodeParent.data:
                        delNodeParent.leftchild = None
                    else:
                        delNodeParent.rightchild = None

            return True

        parent = None
        node = self.root

        # find node to remove
        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.leftchild
            elif data > node.data:
                node = node.rightchild

        # case 1: data not found
        if node is None or node.data != data:
            return False

        # case 2: remove-node has no children
        elif node.leftchild is None and node.rightchild is None:
            if data < parent.data:
                parent.leftchild = None
            else:
                parent.rightchild = None
            return True

        # case 3: remove-node has left child only
        elif node.leftchild and node.rightchild is None:
            if data < parent.data:
                parent.leftchild = node.leftchild
            else:
                parent.rightchild = node.leftchild
            return True

        # case 4: remove-node has right child only
        elif node.leftchild is None and node.rightchild:
            if data < parent.data:
                parent.leftchild = node.rightchild
            else:
                parent.rightchild = node.rightchild
            return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.rightchild
            while delNode.leftchild:
                delNodeParent = delNode
                delNode = delNode.leftchild

            node.data = delNode.data
            if delNode.rightchild:
                if delNodeParent.data > delNode.data:
                    delNodeParent.leftchild = delNode.rightchild
                elif delNodeParent.data < delNode.data:
                    delNodeParent.rightchild = delNode.rightchild
            else:
                if delNode.data < delNodeParent.data:
                    delNodeParent.leftchild = None
                else:
                    delNodeParent.rightchild = None


bst = Tree()
print(bst.insert(10))
print(bst.insert(5))
print(bst.insert(15))
print(bst.insert(2))
print(bst.insert(12))
print(bst.insert(10))
bst.inorder()
print(bst.remove(5))
bst.inorder()
print(bst.insert(5))
bst.inorder()
print(bst.remove(10))
bst.inorder()
