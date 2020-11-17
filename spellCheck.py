from trie import Trie

def loadWordsTrie():
    """
    Load words from google-10000-english-usa.txt into trie
    """

    f = open('google-10000-english-usa.txt', 'r')
    lines = f.readlines()
    f.close()

    rank = 0        # order of the words by given frequency

    trie = Trie()
    for line in lines:
        rank += 1
        word = line.rstrip() #remove '\n'
        if word == "": continue #slip empty strings
        trie.insert(word, rank)

    return trie


def getWordsDistance1(word, freeSymbol='?'):
    """
    Get list of words at an edit distance of 1
    """


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
    """
    Get list of words at an edit distance of d
    """

    if d==1: return getWordsDistance1(word, freeSymbol)
    wordsPrev = getWordsDistance(word, d-1, freeSymbol)
    words = []
    for w in wordsPrev: words += getWordsDistance1(w, freeSymbol)
    return words