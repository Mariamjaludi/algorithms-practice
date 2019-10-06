class MinHeap
    def __init__(self, array):
        self.heapList = array
        self.length = len(array)

    def push(self, val):
        self.heapList.append(val)
        self.length += 1
        i = self.length - 1
        self.bubbleUp(i)

    def bubbleUp(self, i):
        parentIdx = (i - 2) // 2
        while i > 0 and self.heapList[i] < self.heapList[parentIdx]:
            i, parentIdx = self.swap(self.heapList[i], self.heapList[parentIdx], i, parentIdx)

    def swap(self, a, b, i, parentIdx):
        a, b = b, a
        i = parentIdx
        parentIdx = (i - 2) // 2
        return i, parentIdx

    def pop(self):
        top = self.heapList[0]
        last = self.heapList[-1]
        self.heapList[0] = last
        self.bubbleDown()
        return top

    def bubbleDown(self, i=0):
        val = self.heapList[i]
        leftIdx = 2*i + 1
        rightIdx = 2*i + 2
        children = self.getChildren(leftIdx, rightIdx)
        smaller, sI = self.getSmaller(children)
        while children and val > smaller:
            self.heapList[i], self.heapList[iS] = self.heapList[sI], self.heapList[i]
            i = sI
            leftIdx = 2*i + 1
            rightIdx = 2*i + 2
            children = self.getChildren(leftIdx, rightIdx)
            smaller, sI = self.getSmaller(children)

    def getChildren(self, leftI, rightI):
        children = []
        if leftI < self.length:
            children.append((self.heapList[leftI], leftI))
        if rightI < self.length:
            children.append((self.heapList[rightI], rightI))
        return children

    def getSmaller(self, children):
        if len(children) == 0:
            return float('inf'), None
        if len(children) == 1:
           return children[0]
        else:
            childA, iA = children[0]
            childB, iB = children[1]
            return children[0] if childA < childB else children[1]


class MaxHeap
    def __init__(self, array):
        self.heapList = array
        self.length = len(array)

    def push(self, val):
        self.heapList.append(val)
        self.length += 1
        i = self.length - 1
        self.bubbleUp(i)

    def bubbleUp(self, i):
        parentIdx = (i - 2) // 2
        while i > 0 and self.heapList[i] > self.heapList[parentIdx]:
            i, parentIdx = self.swap(self.heapList[i], self.heapList[parentIdx], i, parentIdx)

    def swap(self, a, b, i, parentIdx):
        a, b = b, a
        i = parentIdx
        parentIdx = (i - 2) // 2
        return i, parentIdx

    def pop(self):
        top = self.heapList[0]
        last = self.heapList[-1]
        self.heapList[0] = last
        self.bubbleDown()
        return top

    def bubbleDown(self, i=0):
        val = self.heapList[i]
        leftIdx = 2*i + 1
        rightIdx = 2*i + 2
        children = self.getChildren(leftIdx, rightIdx)
        bigger, bIdx = self.getBigger(children)
        while children and val < bigger:
            self.heapList[i], self.heapList[bIdx] = self.heapList[bIdx], self.heapList[i]
            i = iS
            leftIdx = 2*i + 1
            rightIdx = 2*i + 2
            children = self.getChildren(leftIdx, rightIdx)
            bigger, bIdx = self.getBigger(children)

    def getChildren(self, leftI, rightI):
        children = []
        if leftI < self.length:
            children.append((self.heapList[leftI], leftI))
        if rightI < self.length:
            children.append((self.heapList[rightI], rightI))
        return children

    def getBigger(self, children):
        if len(children) == 0:
            return float('-inf'), None
        if len(children) == 1:
           return children[0]
        else:
            childA, iA = children[0]
            childB, iB = children[1]
            return children[0] if childA > childB else children[1]
