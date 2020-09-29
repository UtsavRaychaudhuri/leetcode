class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[-1]*len(s)
        m=[]
        for i in range(len(s)):
            if s[i]=='(':
                m.append(i)
            elif len(m)==0:
                continue
            else:
                j=m.pop()
                l[j]=1
                l[i]=1
        gs=0
        ls=0
        for i in range(len(l)):
            if l[i]==-1:
                ls=0
                continue
            else:
                ls+=1
                gs=max(gs,ls)
        return gs

sol=Solution()
print(sol.longestValidParentheses("()()"))