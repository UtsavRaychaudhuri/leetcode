import collections

class Solution:
    def findShortestSubArray(self, nums):
        d=collections.defaultdict(int)
        occurence=collections.defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]]+=1
            if len(occurence[nums[i]])==0:
                occurence[nums[i]]=[i,i]
            else:
                occurence[nums[i]][1]=i
        max=0
        mini=999999999999999
        max_arr=[]
        for i in sorted(d,key=lambda i:d[i],reverse=True):
            if d[i]<max:
                break
            else:
                max_arr.append(i)
                max=d[i]
        for i in max_arr:
            mini=min(mini,occurence[i][1]-occurence[i][0])
        return mini+1
        
        
sol=Solution()
sol.findShortestSubArray([1,2,2,3,1])
