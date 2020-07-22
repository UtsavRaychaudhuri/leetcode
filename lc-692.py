import collections
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        return_array=[]
        for i in collections.Counter(["ad","ab"]).most_common(2):
            return_array.append(i[0])
        return return_array

sol=Solution()
print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))