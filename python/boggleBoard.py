# board is a 2D matrix, words is a list of strings
def boggleBoard(board, words):



# gets all the neighboring nodes of the current node
# takes in current node's location and the board matrix
def getNeighbors(i, j, board):
    neighbors = []
    # if current is not the top row and not in the top column
    if i > 0 and j > 0:
        # append the node one row up, one column left
        neighbors.append([i - 1, j - 1])
    # if current is not in the top row and not in the last column
    if i > 0 and j < len(board[0]) - 1:
        # append the node that is one row up, one column right
        neighbors.append([i - 1, j + 1])
    # if current is not in the last row and the last column
    if i < len(board) - 1 and j < len(board[0]) - 1:
        # append the node one row down, one column right
        neighbors.append([i + 1, j + 1])
    # if current is not in the last row and first column
    if i < len(board) - 1 and j > 0:
        # append the node one row down, one column left
        neighbors.append([i + 1, j - 1])
    # if current is not in the top row
    if i > 0:
        # append node one row above (same column)
        neighbors.append([i - 1, j])
    # if current is not in the last row
    if i < len(board) - 1:
        # append the node one row below (same column)
        neighbors.append([i + 1, j])
    # if current is not in the first column
    if j > 0:
        # append node to left (same row)
        neighbors.append([i, j - 1])
    # if current is not in the last column
    if j < len(board[0] - 1):
        # append node to the right (same row)
        neighbors.append([i, j + 1])
    return neighbors    


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def addWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = word

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
