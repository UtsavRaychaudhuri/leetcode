class TrieNode:
    def __init__(self):
        self.val={}
        self.eow=False

class Solution(object):
    def __init__(self):
        self.root=TrieNode()
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict=set(dict)
        for word in dict:
            current=self.root
            for i in word:
                if i not in current.val:
                    current.val[i]=TrieNode()
                current=current.val[i]
            current.eow=True
        final_sentence=""
        for word in sentence.split(" "):
            local_word=""
            current=self.root
            for i in word:
                if i not in current.val or current.eow:
                    break
                local_word+=i
                current=current.val[i]
            if local_word=="":
                final_sentence+=word + " "
            elif local_word in dict:
                final_sentence+=local_word + " "
            else:
                final_sentence+=word + " "
        return final_sentence

sol=Solution()
sol.replaceWords(dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery")





        