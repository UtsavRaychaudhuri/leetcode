import collections

class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned=set(banned)
        max=0
        paragraph=paragraph.replace(","," ").replace("!"," ").replace("?"," ").replace("'"," ").replace(";"," ").replace("."," ").split(" ")
        d=collections.defaultdict(int)
        for i in paragraph:
            if i=="":
                continue
            word=i.lower()
            if word not in banned:
                d[word]+=1
                if d[word]>max:
                    max=d[word]
                    res=word
        return res

sol=Solution()
sol.mostCommonWord("a, a, a, a, b,b,b,c, c",
["a"])