class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits=[]
        for i in range(300):
            self.hits.append([0,0])

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if self.hits[timestamp%300][1]!=timestamp:
            self.hits[timestamp%300][1]=timestamp
            self.hits[timestamp%300][0]=1
        else:
            self.hits[timestamp][0]+=1 
        
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        cnt=0
        for i in self.hits:
            if i[1]>=timestamp-300:
                cnt+=i[0]
        return cnt

counter=HitCounter()
#hit at timestamp 1.
counter.hit(1)

# // hit at timestamp 2.
counter.hit(2)

# // hit at timestamp 3.
counter.hit(3)

# // get hits at timestamp 4, should return 3.
print(counter.getHits(4))

# // hit at timestamp 300.
counter.hit(300)

# // get hits at timestamp 300, should return 4.
print(counter.getHits(300))

# // get hits at timestamp 301, should return 3.
print(counter.getHits(304))