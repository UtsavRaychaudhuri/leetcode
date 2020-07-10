class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        h=len(nums)-1
        m=int((l+h)/2)
        return self.findmin(nums,l,m,h)

    def findmin(self,nums,low,mid,high):
            if nums[low]<=nums[mid]<=nums[high]:
                return nums[low]
            elif nums[high]<=nums[low]<=nums[mid]:
                low=mid+1
                mid=int((low+high)/2)
                return self.findmin(nums,low,mid,high)
            elif nums[mid]<=nums[high]<=nums[low]:
                high=mid
                mid=int((low+high)/2)
                return self.findmin(nums,low,mid,high)
        