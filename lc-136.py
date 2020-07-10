class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_set=set()
        for i in nums:
            if i in my_set:
                my_set.discard(i)
            else:
                my_set.add(i)
        return my_set.pop()
        