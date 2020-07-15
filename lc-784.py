class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        """
        def backtrack(s,current_str):
            self.my_set.add(current_str)
            for i in range(len(s)):
                if s[i].isdigit():
                    continue
                else:
                    current_str = s[:i]+s[i].lower()+s[i+1:]
                    if current_str not in self.my_set:
                        backtrack(s,current_str)
                    elif s[:i]+s[i].upper()+s[i+1:] not in self.my_set:
                        backtrack(s,s[:i]+s[i].upper()+s[i+1:])
                    else:
                        return
        self.my_set=set()
        # self.my_set.add(s)
        backtrack(s,s)
        print("abc")

sol=Solution()
sol.letterCasePermutation("abc")
                    
                