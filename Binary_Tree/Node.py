class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True


    def find(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.data))
            if self.leftchild:
                self.leftchild.preorder()
            if self.rightchild:
                self.rightchild.preorder()

    def postorder(self):
        if self:
            if self.leftchild:
                self.leftchild.postorder()
            if self.rightchild:
                self.rightchild.postorder()
            print(str(self.data))

    def inorder(self):
        if self:
            if self.leftchild:
                self.leftchild.inorder()
            print(str(self.data))
            if self.rightchild:
                self.rightchild.inorder()
