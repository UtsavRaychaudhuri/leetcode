class Solution:
    def shortestWordDistance(self, words, word1, word2):
        j=0
        left,right=-1,-1
        maxd=99999999999
        for i in words:
            if word1==word2:
                if i==word1:
                    if left>=0:
                        right=j
                        maxd=min(maxd,abs(left-right))
                        left=j
                    else:
                        left=j
                        if right>=0:
                            maxd=min(maxd,abs(left-right))
                j+=1
                continue
            if i==word1:
                left=j
                if right>=0:
                    maxd=min(maxd,abs(left-right))
            if i==word2:
                right=j
                if left>=0:
                    maxd=min(maxd,abs(left-right))
            j+=1
        return maxd-1

sol=Solution()
sol.shortestWordDistance([4,2],4,2)