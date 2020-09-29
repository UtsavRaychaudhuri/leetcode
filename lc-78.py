class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr=[[]]
        for i in nums:
            for j in range(len(arr)):
                arr.append(arr[j]+[i])
        return arr
                
sol=Solution()
sol.subsets([1,2,3])