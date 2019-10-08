class NAryTree:

    def __init__(self, root):
        self.root = root
        self.children = []


    def addChildren(self, array):
        for child in array:
            c = NAryTree(child)
            self.children.append(c)
