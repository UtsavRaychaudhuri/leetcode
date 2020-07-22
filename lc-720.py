class Solution:
    def __init__(self):
        self.root={}
    def longestWord(self, words):
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

sol=Solution()
print(sol.longestWord(["sg","qgca","s","qzu","qzub","qzubvs","hlyc","hl","qg","qzubv","qgc","qgcab","qz","sgs","sgsnyn","hly","hlycf","sgsn"]))


