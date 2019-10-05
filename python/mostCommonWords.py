# Most Common Words
# Amazon is partnering with the linguistics department at a local university to
# analyze important works of English literature and identify patterns in word
# usage across different eras. To ensure a cleaner output. the linguistics
# department has provided a list of commonly used words
# (e.g., “an”, “the”. etc.) to exclude from the analysis. In the context of this
# search, a word is an alphabetic sequence of characters having no whitespace or
# punctuation.

# Write an algorithm to find the most frequently used word in the text excluding
# the commonly used words.

# The input to the function/method consists of two arguments:
# literatureText: a string representing the block of text,
# wordsToExclude: a list of strings representing the commonly used words to be
# excluded while analyzing the word frequency.
import re
literatureText = "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack’s and Jill’s favorite food."
wordsToExclude = ['and', 'he', 'the', 'to', 'is', "Jack", "Jill"]

def mostCommonWords(literatureText, wordsToExclude):
    s = re.sub(r'[^\w\s]',' ', literatureText)
    sArr = s.split(" ")
    words = {}
    for word in sArr:
        if word in wordsToExclude or word == "":
            continue
        if word.lower() in words:
            words[word.lower()] += 1
        else:
            words[word.lower()] = 1

    countM = max(words.values())
    winner = []
    for word, count in words.items():
        if count == countM:
            winner.append(word)

    return winner

print(mostCommonWords(literatureText, wordsToExclude))
