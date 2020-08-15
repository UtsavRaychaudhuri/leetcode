class Solution(object):
    def reorganizeString(self, s):
        """
        :type S: str
        :rtype: str
        """
        l,r=0,1
        ans=""
        se=set()
        while(r<len(s)):
            if l in se:
                l+=1
                continue
            if l==r:
                r+=1
                continue
            if s[l]!=s[r]:
                if len(ans)>0:
                    if ans[-1]==s[l]:
                        ans+=s[r]+s[l]
                    else:
                        ans+=s[l]+s[r]
                else:
                    ans+=s[l]+s[r]
                se.add(r)
                l+=1
            r+=1
        if len(ans)>0:
            if ans[-1]!=s[l]:
                ans+=s[l]
        else:
            ans+=s[l]
        if len(ans)>=len(s):
            return ans[:len(s)]
        else:
            return ""

sol=Solution()
print(sol.reorganizeString("baaba"))