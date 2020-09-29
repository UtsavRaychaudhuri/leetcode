from bisect import bisect_left
class MyCalendar(object):

    def __init__(self):
        self.ts=[]
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        arr=self.ts
        idx=bisect_left(arr,[start,end])
        if idx<len(arr):
            if end>arr[idx][0]:
                return False
        if idx>0:
            if start<arr[idx-1][1]:
                return False
        arr.insert(idx,[start,end])
        return True
        
# ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
# [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
sol=MyCalendar()
sol.book(1,5)
sol.book(5,7)
sol.book(7,9)
sol.book(35,48)
sol.book(8,25)