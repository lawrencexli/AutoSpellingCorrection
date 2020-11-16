"""
autocorrect version of the spelling check program
using Trie and SymSpell application
"""
from testing import *
from LCS import lcs

def spellcheck(input, trie):
    if (trie.search(input)):
        return input
    words = getWordsDistance(input, 2)
    possibleWords = []
    for word in words:
        possibleWords += trie.matchAll(word)

    best_match = 0
    best_word = ""
    for candidate in possibleWords:
        if lcs(input, candidate) > best_match:
            best_match = lcs(input, candidate)
            best_word = candidate
    return best_word


if __name__ == "__main__":
    dict_trie = loadWordsTrie()

    #You need to manually end the loop
    while (True):
        print('Enter a word:')
        userInput = input()
        t1 = time.time()
        result = spellcheck(userInput,dict_trie)
        if (len(result) == 0):
            print("Unable to find matches")
        else:
            print(result)
        print("Total time taken: "+str(time.time() - t1))

