class Solution:
    def productExceptSelf(self, nums):
        
        # The length of the input array 
        length = len(nums)
        l=[1]*(length)
        m=[1]*(length)
        n=[1]*(length)
        for i,v in enumerate(nums):
            if i==0:
                l[i]=1
            else:
                l[i]=v*l[i-1]
        print(l)
        

sol=Solution()
sol.productExceptSelf([1,2,3,4])
            
