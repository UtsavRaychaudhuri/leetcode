class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==0 or k==0:
            return 0
        self.ways=0
        self.memo=[]
        for i in range(n+1):
            self.memo.append([-1]*(k+1))
        def backtrack(n,k,arr):
            if n==self.posts:
                self.ways+=1
            print(n,arr,self.ways)
            if n>self.posts:
                return
            for i in range(k):
                if len(arr)>=2:
                    if arr[-2]==arr[-1]==i:
                        continue
                backtrack(n+1,k,arr+[i])
        self.posts=n
        backtrack(0,k,[])
        return self.ways
        
sol=Solution()
print(sol.numWays(n=4,k=2))