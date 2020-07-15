class TrieNode:
    def __init__(self):
        self.val=[None]*26
        self.eow=False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current=self.root
        for i in word:
            index=ord(i)-ord('a')
            if current.val[index] is None:
                current.val[index]=TrieNode()
            current=current.val[index]
        current.eow=True
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current=self.root
        for i in word:
            index=ord(i)-ord('a')
            if current.val[index] is None:
                return False
            current=current.val[index]
        return current.eow
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current=self.root
        for i in prefix:
            index=ord(i)-ord('a')
            if current.val[index] is None:
                return False
            current=current.val[index]
        return True
        
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.startsWith("app")