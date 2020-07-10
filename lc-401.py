class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hr=[8,4,2,1]
        min=[32,16,8,4,2,1]
        self.my_set=set()

        def backtrack(n,hr,min,hour,minute,goal_state,hour_set,min_set):
            if len(str(minute))==1:
                strmin="0"+str(minute)
            else:
                strmin=str(minute)
            stringtocheck=str(hour)+":"+strmin
            if n==goal_state and stringtocheck not in self.my_set:
                self.my_set.add(stringtocheck)
                return
            for i in hr:
                if n+1<=goal_state and hour+i<12 and i not in hour_set:
                    backtrack(n+1,hr,min,hour+i,minute,goal_state,hour_set+[i],min_set)
                for j in min:
                    if n+1<=goal_state and minute+j<60 and j not in min_set:
                        backtrack(n+1,hr,min,hour,minute+j,goal_state,hour_set,min_set+[j])
                    else:
                        return
        backtrack(0,hr,min,0,0,num,[],[])
        return self.my_set
        
        