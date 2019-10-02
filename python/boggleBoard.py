class Trie:
    def __init__(self, stringArr):
        self.root = {}
        self.endSymbol = "*"
        self.populateTrie(stringArr)

    def populateTrie(self, stringArr):
        for string in range(len(stringArr)):
            self.insertSubstringStartingAt(string)

    def insertSubstringStartingAt(self, string):
        node = self.root
        for i in range(len(string)):
            if string[i] not in node:
                node[string[i]] = {}
            node = node[string[i]]
        node[self.endSymbol] = string

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
