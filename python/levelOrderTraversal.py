# You are given a pointer to the root of a binary tree. You need to print the
# level order traversal of this tree. In level order traversal, we visit the
# nodes level by level from left to right. You only have to complete the
# function.


from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def levelOrder(root):
    # Write your code here
    vals = []
    q = deque([root])
    while q:
        node = q.popleft()
        vals.append(str(node.info))
        children = getChildren(node)
        for child in children:
            q.append(child)

    print(" ".join(vals))


def getChildren(node):
    children = []
    if node.left:
        children.append(node.left)
    if node.right:
        children.append(node.right)
    return children


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
