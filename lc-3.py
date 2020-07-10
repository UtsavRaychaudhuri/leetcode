class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        i=max=0
        j=1
        my_dict={s[0]:0}
        while j<len(s):
            if s[j] in my_dict:
                max=j-i if j-i>max else max
                i=my_dict[s[j]]+1 if my_dict[s[j]]+1>i else i
            my_dict[s[j]]=j
            j+=1
        max=j-i if j-i>max else max
        return max