from bisect import bisect_left
class MyCalendarTwo(object):

    def __init__(self):
        self.ts=[]
        self.ds=[]
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        arr=self.ts
        arr2=self.ds
        def db(arr,start,end):
            lf=bisect_left(arr,[start,end])
            if lf<len(arr):
                if arr[lf][0]<=end:
                    return True
            if lf>0:
                if arr[lf-1][1]>=start:
                    return True
            arr.insert(lf,[start,end])
            return False
                    
        lf=bisect_left(arr,[start,end])
        if lf<len(arr):
            if arr[lf][0]<end:
                if db(arr2,start,end):
                    return False
        if lf>0:
            if arr[lf-1][1]>start:
                if db(arr2,start,end):
                    return False
        arr.insert(lf,[start,end])
            
        
cal=MyCalendarTwo()
cal.book(10, 20)
cal.book(50, 60)
cal.book(10, 40)
cal.book(5, 15)
cal.book(5, 10)
cal.book(25, 55)