class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        my_map={}
        tobesorted=[]
        my_arr=[]
        for i in arr2:
            my_map[i]=0
        for i in arr1:
            if i in my_map:
                my_map[i]+=1
            else:
                tobesorted.append(i)
        for i in arr2:
            temp_arr=[i]*my_map[i]
            my_arr+=temp_arr
        return my_arr+sorted(tobesorted)
        