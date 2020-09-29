class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        res=0
        digit=""
        s=s.replace(" ","")
        if len(s)==1:
            return s[0]
        s=s[::-1]
        for i in s:
            if i==" ":
                continue
            if i=="(":
                if digit!="":
                    stack.append(int(digit))
                    digit=""
                while(True):
                    ele1=stack.pop()
                    sign=stack.pop()
                    if sign==")":
                        break
                    ele2=stack.pop()
                    res=ele1+ele2 if sign=="+" else ele2-ele1
                    stack.append(res)
                stack.append(res)
                continue
            if i in ("+","-"):
                if digit!="":
                    stack.append(int(digit))
                stack.append(i)
                digit=""
            elif i.isdigit():
                digit+=i
            else:
                stack.append(i)
        while(stack):
            if digit!="":
                stack.append(int(digit))
                digit=""
            ele=stack.pop()
            sign=stack.pop()
            ele1=stack.pop()
            res=ele+ele1 if sign=="+" else ele1-ele
            if len(stack)==0:
                return res
            stack.append(res)

sol=Solution()
sol.calculate("0   ")