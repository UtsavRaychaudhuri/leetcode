import collections

class Solution(object):
    def subarraysDivByK(self, A, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        sum=0
        res=0
        d=collections.defaultdict(int)
        for i in range(len(A)):
            sum+=A[i]
            
            if sum%k==0:
                res+=1
            if sum-k in d:
                res+=d[sum-k]
            if sum in d:
                res+=d[sum]
                res+=1
            if A[i]%k==0:
                res+=1
            d[sum]+=1
        return res
            
            
sol=Solution()
sol.subarraysDivByK(A = [4,5,0,-2,-3,1], k = 5)