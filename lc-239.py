from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        left,right=0,0
        max=-999999999
        index=0
        q=deque([])
        for i in range(k):
            if nums[i]>max:
                max=nums[i]
                index=i
            q.append(nums[i])
        def search(nums,left,k):
            largest=left
            for i in range(left+1,k):
                if nums[i]>nums[largest]:
                    largest=i
            return largest
        right=k
        left=1
        right=k
        ans=[max]
        for i in range(k,len(nums)):
            if nums[i]>nums[index]:
                index=i
            if left>=index:
                index=search(nums,left,left+k)
            ans.append(nums[index])
            left+=1
            right+=1
        return ans
            
sol=Solution()
sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],2)