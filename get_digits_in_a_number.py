class Solution(object):
    def getdigitsinanumber(self,number):
        while(number>9):
            unitsdigit=number%10
            tensdigit=int(number/10)
            number=tensdigit
            print(unitsdigit,tensdigit)
        print(number)

sol=Solution()
sol.getdigitsinanumber(1234)

