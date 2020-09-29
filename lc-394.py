class Solution(object):
    def decodeString(self, s):
        stack=[]
        res=''
        prev=''
        digit=0
        for i in s:
            if i=='[':
                stack.append(prev)
                stack.append(digit)
                prev=''
                digit=0
            elif i==']':
                digit=stack.pop()
                prevres=stack.pop()
                res=res+prevres+(prev*digit)
                digit=0
            elif i.isdigit():
                digit=digit*10+int(i)
            elif i.isalpha():
                prev+=i
        return res+prev
                
sol=Solution()
sol.decodeString("3[a2[c]]")