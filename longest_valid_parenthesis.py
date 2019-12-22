class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest=0
        local_longest=0
        my_stack=[]
        for i in s:
            if i=="(":
                my_stack.append(i)
            elif len(my_stack)!=0:
                if my_stack.pop()=="(":
                    local_longest+=2
                    if local_longest>longest:
                        longest=local_longest
                else:
                    local_longest=0
            else:
                local_longest=0
        return longest
sol=Solution()
print(sol.longestValidParentheses("()(()"))
