class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        noofone=0
        for i in bin(n)[2:]:
            if i=='1':
                noofone+=1
        return noofone
        