class Solution:
    def addOperators(self, num, target):
        self.out=[]
        nums=[]
        def subsetsum(num,val,n,targetstr):
            if n==len(num):
                if val==target:
                    self.out.append(targetstr)
                    return 
                return
            subsetsum(num,val*num[n],n+1,targetstr+"*"+str(num[n]))
            subsetsum(num,val+num[n],n+1,targetstr+str(val)+"+"+str(num[n]))
            subsetsum(num,val-num[n],n+1,targetstr+"-"+str(num[n]))
        for i in num:
            nums.append(int(i))
        subsetsum(nums,nums[0],1,"")
        return self.out

sol=Solution()
sol.addOperators(num = "232", target = 8)