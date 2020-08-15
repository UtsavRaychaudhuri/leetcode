class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result=""
        if len(num2)>len(num1):
            num1,num2=num2,num1
        num1,num2=list(num1),list(num2)
        limit=-(len(num1))
        for i in range(-1,limit,-1):
            if i<=-len(num2):
                l=0
            else:
                l=int(num2[i])
            k=int(num1[i])
            str((k+l)%10)+result
            if i<-len(num1):
                num1[i]+



            

sol=Solution()
sol.addStrings("123","23")