# board is a 2D matrix, words is a list of strings
def boggleBoard(board, words):

    # add all the words to the tree
    trie = Trie()
    for word in words:
        trie.addWord(word)

    # hash that will hold found words
    finalWords = {}

    # create our visited board:
    visited = [[False for letter in row] for row in board]

    # traverse the whole board
    for i in range(len(board)):
        for j in range(len(board[0])):
            explore(i, j, trie.root, visited, finalWords)
    return list(finalWords.keys())

def explore(i, j, board, trieNode, visited, finalWords):
    # if the current node has been visited, go back
    if visited[i][j]:
        return
    letter = board[i][j]
    # if the letter is not in the trie node, return
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]

    # if we have reached the end of a word and we find a *, store the word
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True

    # if our letter was found at the trieNode, we get its neighbors and explore them
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)

    # uncheck the visited after we have explored a node
    visited[i][j] = False

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
