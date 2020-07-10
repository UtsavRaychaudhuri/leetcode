class Solution:
    
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.global_val=[]
        self.backtrack(0,[],candidates,target)
        return self.global_val

    def backtrack(self,current_val,combination,candidates,target):
        if current_val==target:
            combination.sort()
            if combination not in self.global_val:
                self.global_val.append(combination.copy())
            return
        for i in candidates:
            if current_val+i<=target:
                self.backtrack(current_val+i,combination+[i],candidates,target)
            else:
                return