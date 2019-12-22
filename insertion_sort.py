# start from i=1 to length of the array
# assighn j to i
# while j>0
#     while array[j-1]>a[j]
#         swap the elements
#         decrement j
# [5   4   3   2  1 ]
#     i,j
#     check if 4<5 and j has not reached the start of the array,because when it has reached we know that 
#     there is nothing to sort. I will go from 1 to n thus remembering till where have we sorted. Thus what
#     j will do is take the ith value and put it in the right place in the array by swaping.

a=[5,4,3,2,1]
for i in range(1,len(a)):
    j=i
    while j>0 and a[j]<a[j-1]:
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
    
print(a)
