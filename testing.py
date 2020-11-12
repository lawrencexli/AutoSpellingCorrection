from queue import PriorityQueue
from trie import Trie2
import time

def loadWordsTrie():
    f = open('wordlist.txt', 'r') 
    lines = f.readlines()
    f.close()

    trie = Trie2()
    for line in lines:
        word = line.rstrip()
        if word == "": continue
        trie.insert(word)

    return trie


def getWordsDistance1(word, freeSymbol='?'):

    possibleWords = []

    #Insert
    for i in range(0, len(word)+1):
        newWord = word[:i] + freeSymbol + word[i:]
        possibleWords.append(newWord)

    #remove 
    for i in range(0, len(word)):
        newWord = word[0:i] + word[i+1:]
        possibleWords.append(newWord)

    #replace
    for i in range(0, len(word)):
        newWord = word[0:i] + freeSymbol + word[i+1:]
        possibleWords.append(newWord)


    return possibleWords


def getWordsDistance(word, d, freeSymbol='?'):

    if d==1: return getWordsDistance1(word, freeSymbol)
    wordsPrev = getWordsDistance(word, d-1, freeSymbol)
    words = []
    for w in wordsPrev: words += getWordsDistance1(w, freeSymbol)
    return words



#Testing
if __name__ == "__main__":

    trie = loadWordsTrie()

    print("words loaded")

    # matches = trie.matchAll("ap???")
    # print(matches)



    t1 = time.time()
    words = getWordsDistance("aple", 2)

    possibleWords = []
    for word in words:
        possibleWords += trie.matchAll(word)
    totalTime = time.time()-t1

    print(words)
    print(possibleWords)
    print(totalTime)