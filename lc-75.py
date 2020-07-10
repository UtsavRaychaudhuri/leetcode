class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_pointer=0
        one_pointer=0
        two_pointer=0
        for j in range(len(nums)):
            if nums[j]==1:
                if nums[two_pointer]==2:
                    nums[two_pointer],nums[j]=nums[j],nums[two_pointer]
                    two_pointer+=1
                    if nums[one_pointer]!=1:
                        one_pointer=two_pointer-1
                if nums[one_pointer]!=1:
                    one_pointer=j
            elif nums[j]==0:
                if nums[two_pointer]==2:
                    nums[two_pointer],nums[j]=nums[j],nums[two_pointer]
                    two_pointer+=1
                    if nums[one_pointer]==1:
                        nums[one_pointer],nums[two_pointer-1]=nums[two_pointer-1],nums[one_pointer]
                        one_pointer+=1
                elif nums[one_pointer]==1:
                    nums[j],nums[one_pointer]=nums[one_pointer],nums[j]
                    one_pointer+=1
            else:
                if nums[two_pointer]!=2:
                    two_pointer=j
            
                    
                
        