class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word, frequency = -1):
        """
        Insert word to Trie
        """
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                newN = Node()
                cur.children[c] = newN
                cur = newN
        cur.isEnd = True
        cur.freq = frequency

    def search(self, word):
        """
        Checks if word exist in Trie
        """
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return cur.isEnd == True

    def findFreq(self, word):
        """
        Find the words frequency
        """
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return -1

        if cur.isEnd == True:
            return cur.freq
        else:
            return -1

    def matchAll(self, word, freeSymbol='?'):
        """
        Returns a list of all matching words in the Trie that can be obtained by replacing the '?' (or freeSymbol) characters
        Wrapper for __matchAllR
        """
        return self.__matchAllR(word, self.root, freeSymbol)

    def __matchAllR(self, word, cur, freeSymbol):
        """
        Recursive function to get alll matching words by replacing the '?' (or given freeSymbol) character
        word: input word
        cur: current node in the Trie
        freeSymbol: symbol to use for the unknown characters (usually '?')
        """
        words = []  # List of words to be returned

        missing = word  # part of the word that hasn't been explored yet
        explored = ""  # part of the word that was explored already
        loopBroken = False
        for c in word:
            missing = missing[1:]

            if c == freeSymbol:  # if character is (?) or unknown

                # Recursively call function in the remaining of the word with every possible children
                for childVal, childNode in cur.children.items():
                    newEnds = self.__matchAllR(missing, childNode, freeSymbol)

                    for end in newEnds:
                        words.append(explored + childVal + end)

                loopBroken = True
                break

            explored += c

            if c in cur.children:
                cur = cur.children[c]
            else:
                return []

        if not loopBroken and cur.isEnd:
            words += [word]
        return words


class Node:
    """
    Node to use in the Trie
    """
    def __init__(self):
        self.children = {}  # dictionary to represent children
        self.isEnd = False  # wheither this node is the end of a word
        self.freq = -1

