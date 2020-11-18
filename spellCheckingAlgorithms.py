from spellCheck import *

def spellcheck_popularity(word_input, trie):
    """
    takes a word, word_input, and a trie to search for that word
    returns the word that is most common in the resulting possible words
    """

    if (trie.search(word_input)): return word_input
    
    possibleWords = getAllWordMatches(word_input, trie, 1)
    if len(possibleWords) == 0: possibleWords = getAllWordMatches(word_input, trie, 2)

    lowest_rank = 11000
    best_word = ""
    cur_rank = 0

    for candidate in possibleWords:
        cur_rank = trie.findFreq(candidate)
        if cur_rank != -1 and cur_rank < lowest_rank:
            lowest_rank = cur_rank
            best_word = candidate

    return best_word

def spellcheck_appearances(word_input, trie):
    """
    takes a word, word_input, and a trie to search for that word
    returns the word with the most appearances in the set of words with edit 
    distance 2
    """

    if (trie.search(word_input)): return word_input

    possibleWords = getAllWordMatches(word_input, trie, 1)
    if len(possibleWords) == 0: possibleWords = getAllWordMatches(word_input, trie, 2)


    popularity = {}
    for candidate in possibleWords:
        if candidate not in popularity:
            popularity[candidate] = 1
        else:
            popularity[candidate] += 1

    best_match = 0
    best_word = ""

    for candidate in popularity:
        if popularity[candidate] > best_match:
            best_match = popularity[candidate]
            best_word = candidate


    return best_word


def spellcheck_LCS(word_input, trie):
    """
    Returns the word within the set of words with edit distance 2 with the largest LCS
    """

    if (trie.search(word_input)): return word_input

    possibleWords = getAllWordMatches(word_input, trie, 2)


    best_match = 0
    best_word = ""
    for candidate in possibleWords:
        if lcs(word_input, candidate) > best_match:
            best_match = lcs(word_input, candidate)
            best_word = candidate
    return best_word