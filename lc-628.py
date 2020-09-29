import sys

class Solution:
    def maximumProduct(self, nums):
        max0=max1=max2=-sys.maxsize
        min0=min1=min2=sys.maxsize
        for i in nums:
            if i<min2:
                min2=i
                if min2<min1:
                    min2,min1=min1,min2
                    if min1<min0:
                        min1,min0=min0,min1
            if i>max0:
                max0=i
                if max0>max1:
                    max0,max1=max1,max0
                    if max1>max2:
                        max1,max2=max2,max1

        return max(max0*max1*max2,min0*min1*min2)
sol=Solution()
print(sol.maximumProduct([-1,-2,-3,4]))
