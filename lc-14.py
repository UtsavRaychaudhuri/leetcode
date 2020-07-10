class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        notfound=False
        common_prefix=""
        if len(strs)==1:
            return strs[0]
        try:
            for i in range(len(strs[0])):
                for j in range(1,len(strs)):
                    if strs[j-1][i]!=strs[j][i]:
                        notfound=True
                        break
                if notfound:
                    break
                else:
                    common_prefix+=strs[j][i]
        except:
            return common_prefix
        return common_prefix  

                    
                    
                
        