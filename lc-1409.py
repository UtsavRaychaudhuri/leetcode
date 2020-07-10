class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        return_this=[]
        my_arr=list()
        for i in range(1,m+1):
            my_arr.append(i)
        for i in queries:
            ind = my_arr.index(i)
            my_arr.insert(0,my_arr.pop(ind))
            return_this.append(ind)
        return return_this
        