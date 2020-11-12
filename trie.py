

class Trie:

    def __init__(self):

        self.root = Node()


    def insert(self, word):

        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                newN = Node()
                cur.children[c] = newN
                cur = newN
        cur.isEnd = True


    def search(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
                
        return cur.isEnd == True
                
class Trie2(Trie):


    def matchAll(self, word, freeSymbol='?'):
        return self.__matchAllR(word, self.root, freeSymbol)

    def __matchAllR(self, word, cur, freeSymbol):

        words = []
        
        missing = word
        explored = ""
        loopBroken = False
        for c in word:
            missing = missing[1:]

            if c == freeSymbol:
                
                for childVal, childNode in cur.children.items():
                    newEnds = self.__matchAllR(missing, childNode, freeSymbol)

                    for end in newEnds:
                        words.append(explored + childVal + end)                    
                
                loopBroken = True
                break
                    

            explored += c

            if c in cur.children: cur = cur.children[c]
            else: return []

        if not loopBroken and cur.isEnd: words += [word]
        
        return words
        

class Node:

    def __init__(self):

        self.children = {}
        self.isEnd = False
