class Solution(object):
    def majorityElement(self, num):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(num)[len(num)/2]
                
            
            
        