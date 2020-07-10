class Solution(object):
    def sumOfDigits(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        a=sorted(a)
        s=str(a[0])
        sum=0
        for i in s:
            sum+=int(i)
        if sum%2==0:
            return 1
        return 0
            