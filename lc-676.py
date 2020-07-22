class TrieNode:
    def __init__(self):
        self.val={}
        self.eow=False
        self.visited=False
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_dict={}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for i in dict:
            if len(i) in self.my_dict:
                self.my_dict[len(i)].append(i)
            else:
                self.my_dict[len(i)]=[i]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) in self.my_dict:
            for words in self.my_dict[len(word)]:
                if word==words:
                    continue
                miss=0
                for i in range(len(word)):
                    if word[i]!=words[i]:
                        miss+=1
                        if miss>1:
                            break
                if miss==1:
                    return True
        return False




    


                    
                
                
        


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello", "leetcode"])
param_2 = obj.search("hello")
print(param_2)
param_3= obj.search("leetcoded")
print(param_3)