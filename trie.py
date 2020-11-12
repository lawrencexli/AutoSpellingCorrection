

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
                
            
        

class Node:

    def __init__(self):

        self.children = {}
        self.isEnd = False
