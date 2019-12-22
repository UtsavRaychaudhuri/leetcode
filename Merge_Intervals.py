class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals)
        for i,v in enumerate(intervals):
            j=i+1
            while(j<len(intervals)):
                if v[1]>=intervals[j][0]:
                    intervals[i][1]=intervals[j][1]
                    intervals.pop(j)
                else:
                    break
        return intervals
    
sol=Solution()
print(sol.merge([[1,3],[2,6],[8,10],[10,18]]))