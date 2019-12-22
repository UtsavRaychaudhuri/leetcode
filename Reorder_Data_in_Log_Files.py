class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        return sorted(filter(lambda l: l[l.find(" ") + 1].isalpha(), logs), key = lambda x: (x[x.find(" "):], x[:x.find(" ")])) + list(filter(lambda l: l[l.find(" ") + 1].isdigit(), logs))

        


sol=Solution()
sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"])