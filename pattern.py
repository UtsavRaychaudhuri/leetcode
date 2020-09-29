# def doSomething(blob, pattern):
#     #Write your code here
#     i=j=k=0
#     local=0
#     blob_arr=[0]*len(blob)
#     k=1
#     while(k<len(blob)):
#         if blob[k]==blob[i]:
#             blob_arr[k]=i+1
#             i+=1
#             k+=1
#         else:
#             if i!=0:
#                 i=blob_arr[i-1]
#             else:
#                 blob_arr[k]=0
#                 k+=1
#     res=[]
#     local=i=0
#     while(j<len(pattern)):
#         if pattern[j]=="|":
#             res.append(local)
#             local=0
#             i=0
#         elif pattern[j]==blob[i]:
#             i+=1
#             if i==len(blob):
#                 local+=1
#                 if i!=1:
#                     j-=1
#                 i=0
#         else:
#             if i!=0:
#                 i=blob_arr[i-1]
#                 j-=1
#         j+=1
#     res.append(local)
#     res.append(sum(res))
#     res="|".join(str(i) for i in res)
#     print(res)
            

import sys

def doSomething(blob, pattern):
    #Write your code here
    blob="|".join(blob)
    if pattern is '':
        s=["0"]*len(blob.split("|"))
        s.append('0')
        return "|".join(s)
    i=j=k=0
    local=0
    pattern_arr=[0]*len(pattern)
    k=1
    while(k<len(pattern)):
        if pattern[k]==pattern[i]:
            pattern_arr[k]=i+1
            i+=1
            k+=1
        else:
            if i!=0:
                i=pattern_arr[i-1]
            else:
                pattern_arr[k]=0
                k+=1
    res=[]
    local=i=0
    while(j<len(blob)):
        if blob[j]=="|":
            res.append(local)
            local=0
            i=0
        elif blob[j]==blob[i]:
            i+=1
            if i==len(pattern):
                local+=1
                if i!=1:
                    j-=1
                i=0
        else:
            if i!=0:
                i=pattern_arr[i-1]
                j-=1
        j+=1
    res.append(local)
    res.append(sum(res))
    res="|".join(str(i) for i in res)
    return res
            
        
for line in sys.stdin:
    splitted_input = line.split(';')
    pattern = splitted_input[0]
    blobs = splitted_input[1].split('|')
 
    result = doSomething(blobs, pattern)
    print(result)