class TrieNode:
    def __init__(self):
        self.val={}
        self.count=0
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        current=self.root
        for i in key:
            if i not in current.val:
                current.val[i]=TrieNode()
                current.val[i].count=val
            else:
                current.val[i].count+=val
            current=current.val[i]
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum=0
        current=roo
        for i in prefix:
            sum=max(current.val[i].count,sum)
            current=current.val[i]
        return sum
        
        


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple",3)
param_2 = obj.sum("ap")