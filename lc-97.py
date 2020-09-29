import collections

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        def il(s1,i,s2,j,res,s3):
            if res==s3 and i==len(s1) and j==len(s2):
                return True
            ans=False
            if i<len(s1):
                ans|=il(s1,i+1,s2,j,res+s1[i],s3)
            if j<len(s2):
                ans|=il(s1,i,s2,j+1,res+s2[j],s3)
            return ans
        return il(s1,0,s2,0,"",s3)

sol=Solution()
sol.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")