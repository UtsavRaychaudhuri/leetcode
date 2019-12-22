class Solution(object):
    def __init__(self):
        self.dp=[]
        self.lowest=[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
        self.very_low=[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]

    def find_all_permuation(self,nums):
        self.nums=nums[:]
        self.all_permutation(nums)
        if self.lowest==[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]:
            nums=self.very_low
        else:
            nums=self.lowest
        return nums
    def all_permutation(self,nums):
        if nums in self.dp:
            return
        else:
            if nums<self.lowest and nums>self.nums:
                self.lowest=nums[:]
            if nums<self.very_low:
                self.very_low=nums[:]
            new_num=nums[:]
            self.dp.append(new_num)
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                self.all_permutation(nums)

sol=Solution()
print(sol.find_all_permuation([1,2,3]))

