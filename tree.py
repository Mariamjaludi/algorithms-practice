class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left == None:
                return False
            else:
                return self.left.find(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.find(value)

    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()
        print(self.value)
        if self.right != None:
            self.right.printInOrder()

    def bfs(self):
        q = deque([self])
        while q:
            val = q.pop()
            print(val.value)
            if val.left:
                q.appendleft(val.left)
            if val.right:
                q.appendleft(val.right)
