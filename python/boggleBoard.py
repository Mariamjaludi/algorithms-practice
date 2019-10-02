# board is a 2D matrix, words is a list of strings
def boggleBoard(board, words):







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
