class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.final_arr=[]
        self.final_str=set()
        def backtrack(i,candidates,target,combinations,sum_arr,comb_str):
            if sum_arr==target and comb_str not in self.final_str:
                self.final_arr.append(combinations)
                self.final_str.add(comb_str)
                return
            while(i<len(candidates)):
                if sum_arr+candidates[i]<=target:
                    backtrack(i+1,candidates,target,combinations+[candidates[i]],sum_arr+candidates[i],comb_str+str(candidates[i]))
                i+=1
        backtrack(0,candidates,target,[],0,"")
        return self.final_arr
            
        
        