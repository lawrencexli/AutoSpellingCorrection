import time
from spellCheck import *

#Testing
if __name__ == "__main__":

    trie = loadWordsTrie()

    print("words loaded")

    # matches = trie.matchAll("ap???")
    # print(matches)

    t1 = time.time()
    words = getWordsDistance("dsfsdf", 1)

    possibleWords = []
    for word in words:
        possibleWords += trie.matchAll(word)
    totalTime = time.time()-t1

    print(words)
    print(possibleWords)
    print(totalTime)