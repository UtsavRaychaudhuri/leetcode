import collections

class UndergroundSystem(object):

    def __init__(self):
        d=collections.defaultdict(lambda:-1)
        self.ci=collections.defaultdict(lambda:collections.defaultdict(lambda:-1))
        self.avgtime=dict()
        
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.ci[id][stationName]=t

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        for station,time in self.ci[id].items():
            if station+stationName not in self.avgtime and stationName+station not in self.avgtime:
                self.avgtime[station+stationName]=[1,t-time]
            elif station+stationName in self.avgtime:
                self.avgtime[station+stationName][0]+=1
                self.avgtime[station+stationName][1]+=t-time
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return self.avgtime[startStation+endStation][1]/self.avgtime[startStation+endStation][0]
        


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(10,"Leyton",3)
obj.checkOut(10,"Paradise",8)
obj.getAverageTime("Leyton","Paradise")
obj.checkIn(5,"Leyton",10)
obj.checkOut(5, "Paradise", 16)
obj.getAverageTime("Leyton", "Paradise")
obj.checkIn(2, "Leyton", 21)
obj.checkOut(2, "Paradise", 30)
print(obj.getAverageTime("Leyton", "Paradise"))
