class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr=[]
        for i in range(numRows):
            arr.append([])
        j=0
        gofw,gobw=False,False
        for i in s:
            if j==0:
                gofw=True
                gobw=False
                arr[j].append(i)
            elif j==numRows-1:
                gobw=True
                gofw=False
                arr[j].append(i)
            else:
                arr[j].append(i)
            if gofw:
                j+=1
            if gobw:
                j-=1
        res=''
        for i in arr:
            res+=''.join(i)
        return res
sol=Solution()
sol.convert(s = "PAYPALISHIRING", numRows = 4)