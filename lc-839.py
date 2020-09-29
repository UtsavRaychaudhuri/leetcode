class Solution:
    def numSimilarGroups(self, A):
        b=[]
        a=[]
        def check(word,a):
            for i in range(len(a)):
                vi=0
                for k in range(len(word)):
                    if word[k] not in a[i][k]:
                        vi+=1
                    if vi>2:
                        break
                if vi<=2:
                    for char in range(len(word)):
                        a[i][char].add(word[char])
                    return
            return -1      
        for i in A[0]:
            for j in i:
                b.append(set(j))
        a.append(b)
        for i in A[1:]:
            ret = check(i,a)
            if ret==-1:
                a.append([])
                for j in i:
                    a[-1].append(set(j))
        return len(a)

sol=Solution()
sol.numSimilarGroups(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"])