class Solution(object):
    def __init__(self):
        self.m=-1
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.binary_search(0,int((0+len(nums))/2),len(nums)-1,nums,target)
        return self.m
    
    def binary_search(self,l,m,h,nums,target):
        if h<l or l>h:
            return
        if nums[m]==target:
            self.m=m
            return
        if nums[l]==target:
            self.m=l
            return
        if nums[h]==target:
            self.m=h
            return
        if nums[l]<nums[m]:
            if nums[l]<=target<=nums[m]:
                h=m-1
                m=int((l+h)/2)
            else:
                l=m+1
                m=int((l+h)/2)
        else:
            if nums[m]<=target<=nums[h]:
                l=m+1
                m=int((l+h)/2)
            else:
                h=m-1
                m=int((l+h)/2)
        self.binary_search(l,m,h,nums,target)

sol=Solution()
print(sol.search([4,5,6,7,0,1,2],0))
        
