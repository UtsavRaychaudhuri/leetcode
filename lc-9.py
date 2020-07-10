class Solution(object):
    def isPalindrome(self, Number):
        """
        :type x: int
        :rtype: bool
        """
        Actual = Number
        Reverse = 0    
        while(Number > 0):    
            Reminder = Number %10    
            Reverse = (Reverse *10) + Reminder    
            Number = Number //10
        return Reverse==Actual