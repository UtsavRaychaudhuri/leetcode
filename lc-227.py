class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        cur=0
        number=""
        i=0
        while(i<len(s)):
            if s[i]==" ":
                continue
            if len(stack)>0:
                if stack[-1]=="*" or stack[-1]=="/":
                    sign=stack.pop()
                    number=stack.pop()
                    tmp=""
                    for j in range(i,len(s)):
                        if s[j].isdigit():
                            tmp+=s[j]
                        else:
                            break
                    i=j
                    res=number*int(tmp) if sign=="*" else number//int(tmp)
                    stack.append(res)
                    number=""
                    continue
            if s[i] in ("*","+","/","-"):
                if number!="":
                    stack.append(int(number))
                stack.append(s[i])
                number=""
            if s[i].isdigit():
                number+=s[i]
            i+=1
        while(stack):
            if len(stack)==1:
                return stack[0]
            number1=stack.pop()
            sign=stack.pop()
            number2=stack.pop()
            res=number1+number2 if sign=="+" else number2-number1
            stack.append(res)
        return res
        
sol=Solution()
sol.calculate("0+0-1")