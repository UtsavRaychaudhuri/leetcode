class Solution(object):
    def minSwapsCouples(self, row):
        d=dict()
        ans=0
        for i in range(len(row)):
            d[row[i]]=i
        for i in range(0,len(row),2):
            if row[i+1]!=row[i]^1:
                ans+=1
                num=row[i+1]
                newpos=d[row[i]^1]
                row[d[row[i]^1]],row[i+1]=row[i+1],row[d[row[i]^1]]
                d[row[i+1]]=i+1
                d[num]=newpos
        return ans

sol=Solution()
sol.minSwapsCouples([0,5,4,3,2,1])