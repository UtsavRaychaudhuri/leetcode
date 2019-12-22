class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        s = "abpcplea", d = ["ale","apple","monkey","plea"]
        for i in d:
            my_string=s
            my_word=0
            for j in i:
                if j in my_string:
                    my_string.pop(my_string.index(j))
                    my_word+=1
                else:
                    break
                    
