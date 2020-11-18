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

def getAllWordMatches(word, trie, maxDistance):
    """
    Gets all word matches in the trie within given edit distance
    """

    possibleWords = []
    for word in getWordsDistance(word, maxDistance):
        possibleWords += trie.matchAll(word)

    return possibleWords

def lcs(string1, string2):
    """
    Returns the length of the LCS between the 2 input strings
    """

    c = [[None for i in range(len(string2) + 1)] for j in range(len(string1) + 1)]

    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif string1[i - 1] == string2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c[len(string1)][len(string2)]


def changeWords(text, trie, algorithm):
    """
    Takes unedited text from the text box
    Returns the suggested corrected text
    """
    
    correctedText = ""

    for word in text.split():

        word = word.lower()
        #Check if the word contains any symbols at the end
        if (any(elem in word[-1] for elem in ".,?!();:")):
                # Check if word is already correct
                if (trie.search(word[0:-1])):
                    correctedText += (word[0:-1] + " ")
                # Otherwise, correct the word
                else:
                    corrected = algorithm(word[0:-1], trie)
                    #If the autocorrect cannot find any matches, it will not modify that word
                    if (len(corrected) != 0):
                        correctedText += (word.replace(word[0:-1], corrected) + " ")
                    else:
                        correctedText += (word + " ")
        # Normally ended words
        else:
            # Check if word is already correct
            if (trie.search(word)):
                correctedText += (word + " ")
            # Otherwise, correct the word
            else:
                corrected = algorithm(word, trie)
                #If the autocorrect cannot find any matches, it will not modify that word
                if (len(corrected) != 0):
                    correctedText += (word.replace(word, corrected) + " ")
                else:
                    correctedText += (word + " ")

    return correctedText