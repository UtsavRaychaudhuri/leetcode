class Solution(object):
    def __init__(self):
        self.dp=[]

    def find_all_permuation(self,nums):
        self.all_permutation(nums)
        return self.dp
    def all_permutation(self,nums):
        if nums in self.dp:
            return
        else:
            new_num=nums.copy()
            self.dp.append(new_num)
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                self.all_permutation(nums)

sol=Solution()
print(sol.find_all_permuation([1,2,3,4]))

