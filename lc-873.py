class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        highest=A[-1]
        a=set(A)
        local=2
        found=False
        global_highest=0
        for i in range(len(A)-2):
            for j in range(i+1,len(A)-1):
                k=A[i]
                l=A[j]
                while(k+l<=highest):
                    if k+l in a:
                        found=True
                        k,l=l,k+l
                        local+=1
                    else:
                        break
                if local>global_highest and found:
                    global_highest=local
                local=2
        return global_highest
                
                        
                
        