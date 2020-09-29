class Solution:
    def merge_sort(self,nums):
        def ms(nums):
            if len(nums)==1:
                return
            r=nums[:len(nums)//2]
            l=nums[len(nums)//2:]
            ms(l)
            ms(r)
            tmp=[]
            i,j,k=0,0,0
            while(i<len(l) and j<len(r)):
                if l[i]<r[j]:
                    nums[k]=l[i]
                    i+=1
                else:
                    j+=1
                    nums[k]=r[j]
                k+=1
            while(i<len(l)):
                nums[k]=l[i]
                i+=1
                k+=1
            while(j<len(r)):
                nums[k]=r[j]
                j+=1
                k+=1
            return nums



        return ms(nums)

sol=Solution()
print(sol.merge_sort([5,4,3,2,1]))