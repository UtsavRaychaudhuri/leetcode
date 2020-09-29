class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        globalres,localres=1,1
        while(nums):
            for i in nums:
                break
            if i+1 not in nums and i-1 not in nums:
                nums.remove(i)
            else:
                check=[i]
                nums.remove(i)
                localres=1
                while(check):
                    i=check.pop()
                    if i+1 in nums:
                        nums.remove(i+1)
                        check.append(i+1)
                        localres+=1
                    if i-1 in nums:
                        nums.remove(i-1)
                        check.append(i-1)
                        localres+=1
            globalres=max(localres,globalres)
        return globalres
                    
                        
sol=Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))