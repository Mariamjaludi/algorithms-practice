class BinHeap:
    def __init__(self, array, minHeap=True):
        self.minHeap = minHeap
        self.heapList = array
        self.currentSize = len(array)

    def insert(self, val):
        self.heapList.append(val)
        self.currentSize += 1
        idx = self.currentSize - 1
        self.bubbleUp(idx)

    def bubbleUp(self, i):
        parentIdx = (i - 2) // 2
        while i > 0:
            if minHeap:
                if self.heapList[i] < self.heapList[parentIdx]:
                    i, parentIdx = self.swap(self.heapList[i], self.heapList[parentIdx], i, parentIdx)
                else:
                    break
            else:
                if self.heapList[i] > self.heapList[parentIdx]:
                    i, parentIdx = self.swap(self.heapList[i], self.heapList[parentIdx], i, parentIdx)
                else:
                    break

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
        if self.minHeap:
            self.minBubbleDown(val, i, leftIdx, rightIdx)
        else:
            self.maxBubbleDown(val, i, leftIdx, rightIdx)

    def minBubbleDown(self, val, i, leftIdx, rightIdx):
        children = self.getChildren(leftIdx, rightIdx)
        smaller, iS = self.getSmaller(children)
        while children and val > smaller:
            self.heapList[i], self.heapList[iS] = self.heapList[iS], self.heapList[i]
            i = iS
            leftIdx = 2*i + 1
            rightIdx = 2*i + 2
            children = self.getChildren(leftIdx, rightIdx)
            smaller, iS = self.getSmaller(children)

    def maxBubbleDown(self, val, i, leftIdx, rightIdx):
        children = self.getChildren(leftIdx, rightIdx)
        bigger, iS = self.getBigger(children)
        while children and val < smaller:
            self.heapList[i], self.heapList[iS] = self.heapList[iS], self.heapList[i]
            i = iS
            leftIdx = 2*i + 1
            rightIdx = 2*i + 2
            children = self.getChildren(leftIdx, rightIdx)
            bigger, iS = self.getBigger(children)

    def getChildren(self, leftI, rightI):
        children = []
        if leftI < self.currentSize:
            children.append((self.heapList[leftI], leftI))
        if rightI < self.currentSize:
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

    def getBigger(self, children):
        if len(children) == 0:
            return float('-inf'), None
        if len(children) == 1:
           return children[0]
        else:
            childA, iA = children[0]
            childB, iB = children[1]
            return children[0] if childA > childB else children[1]

    def swap(self, a, b, i, parentIdx):
        a, b = b, a
        i = parentIdx
        parentIdx = (i - 2) // 2
        return i, parentIdx
