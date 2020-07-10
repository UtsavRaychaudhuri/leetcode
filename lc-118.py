class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        final_arr=[[1]]
        old_arr=[]
        for i in range(numRows-1):
            j,new_arr=0,[]
            while(j+1<len(old_arr)):
                new_arr.append(old_arr[j]+old_arr[j+1])
                j+=1
            new_arr.insert(0,1)
            new_arr.insert(len(new_arr),1)
            old_arr=new_arr[:]
            final_arr.append(new_arr)
        return final_arr
        
            
                
                
                
                
        