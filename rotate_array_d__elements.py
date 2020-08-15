from collections import deque
class Solution:
    def rotate_array_d_elements(self,arr,d):
        j=0
        while(j<d):
            j+=1
            arr.append(arr.pop(0))
        return arr

sol=Solution()
test_cases=input()
for i in range(int(test_cases)):
    length=int(input())
    arr=input()
    my_arr=[]
    for i in arr.split(" "):
        my_arr.append(int(i))
    d=int(input())
    print(sol.rotate_array_d_elements(my_arr,d))




