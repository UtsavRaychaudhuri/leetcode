import math
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        my_array=[0]*(num+1)
        log2=math.log10(2)
        best=0
        for i in range(1,len(my_array)):
            log10_2=math.log10(i)/log2
            if math.ceil(log10_2)==math.floor(log10_2):
                my_array[i]=1
                best=i
            else:
                my_array[i]=my_array[i-best]+1
        return my_array
            
        