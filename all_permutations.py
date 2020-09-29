from collections import defaultdict
class Solution:
    def permute(self, nums):
        count=[0]*9
        for i in nums:
            count[i]+=1
        stack=[[]]
        count=[count]
        out=[]
        for i in nums:
            l=len(stack)
            for j in stack[:l]:
                for k in range(len(j)+1):
                    if len(j)==len(nums)-1:
                        out.append(j[:k]+[i]+j[k:])
                        count.append()
                    stack.append(j[:k]+[i]+j[k:])
        return out

sol=Solution()
sol.permute([1,1,3])