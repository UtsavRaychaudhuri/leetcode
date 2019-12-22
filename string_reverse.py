class Solution(object):
    def string_reverse(self,s,i):
        if i==len(s):
            return
        self.string_reverse(s,i+1)
        s[-i-1]=s[i]

sol=Solution()
sol.string_reverse("Hello",0)


