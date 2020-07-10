class Solution(object):
    def plusOne(self, nums):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add=False
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==9:
                add=True
                nums[i]=0
            else:
                nums[i]+=1
                add=False
                break
        if add:
            nums.insert(0,1)
        return nums
                
        
        