class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        numjewels=0
        for i in S:
            if i in J:
                numjewels+=1
        return numjewels
        