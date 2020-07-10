class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        s=""
        for i in S:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                continue
            s+=i
        return s
        