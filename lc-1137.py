class Solution(object):
    def tribonacci(self,n):
        self.my_sum=[0]*(n+1)
        self.tribonacci_utsav(n)
        return self.my_sum[n]
    
    def tribonacci_utsav(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.my_sum[n]!=0:
            return self.my_sum[n]
        if n==0:
            self.my_sum[n]=0
            return 0
        if n==1:
            self.my_sum[n]=1
            return 1
        if n==2:
            self.my_sum[n]=1
            return 1
        self.my_sum[n]=self.tribonacci_utsav(n-1)+self.tribonacci_utsav(n-2)+self.tribonacci_utsav(n-3)
        return self.my_sum[n]