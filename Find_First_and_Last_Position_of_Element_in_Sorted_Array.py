class Solution(object):
    def __init__(self):
        self.m=-1
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        self.binary_search(0,int(len(nums)/2),len(nums)-1,nums,target)
        l,h=self.m,self.m
        try:
            if self.m!=-1:
                while(l>=0):
                    if nums[l]==target:
                        l-=1
                    else:
                        break
                while(h<len(nums)):
                    if nums[h]==target:
                        h+=1
                    else:
                        break
        except:
            pass
        if self.m!=-1:
            return [l+1,h-1]
        return [-1,-1]
                
    def binary_search(self,l,m,h,nums,target):
        if h<l or l>h:
            return
        if nums[l]==target:
            self.m=l
            return
        if nums[m]==target:
            self.m=m
            return
        if nums[h]==target:
            self.m=h
            return
        if nums[m]>target:
            h=m-1
            m=int((h+l)/2)
        else:
            l=m+1
            m=int((h+l)/2)
        self.binary_search(l,m,h,nums,target)

sol=Solution()
sol.searchRange([5,7,7,8,8,10],6)