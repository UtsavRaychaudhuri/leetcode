class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        my_arr=[]
        return_Arr=[]
        k=0
        for i,j in points:
            my_arr.append((i**2+j**2,k))
            k+=1
        my_arr = sorted(my_arr,key=lambda l: l[0])
        for i in my_arr[:K]:
            return_Arr.append(points[i[1]])
        return return_Arr

sol=Solution()
sol.kClosest([[1,3],[-2,2]],1)

