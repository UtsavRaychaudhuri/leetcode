class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        my_dict=dict()
        for i in s:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i]=1
        for i in t:
            if i not in my_dict:
                return False
            if my_dict[i]==1:
                del my_dict[i]
            else:
                my_dict[i]-=1
        return len(my_dict)==0
        