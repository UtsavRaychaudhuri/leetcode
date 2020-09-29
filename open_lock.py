from collections import deque
class Solution:
    def openLock(self, deadends, target):
        t=[]
        for i in target:
            t.append(int(i))
        s=set()
        seen=set()
        for i in deadends:
            t=[]
            for j in i:
                t+=[j]
            s.add(tuple(t.copy()))
        d=deque([-1,[0,0,0,0]])
        level=0
        while(d):
            element=d.pop()
            if element==-1:
                level+=1
                if len(d)==0:
                    return -1
                d.appendleft(-1)
                continue
            for i,v in enumerate(element):
                c=element.copy()
                c[i]=0 if v==9 else v+1
                if c==t:
                    return level
                if tuple(c) not in s and tuple(c) not in seen:
                    d.appendleft(c)
                    seen.add(tuple(c))
                c=element.copy()
                c[i]=9 if v==0 else v-1
                if c==t:
                    return level
                if tuple(c) not in s and tuple(c) not in seen:
                    d.appendleft(c)
                    seen.add(tuple(c))
        return level


        




sol=Solution()
print(sol.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))