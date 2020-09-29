class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        s="Hello"
        import heapq
        heapq.heapify(boxes)
        heapq.heapify(warehouse)
        res=0
        while(boxes and warehouse):
            if boxes[0]<=warehouse[0]:
                heapq.heappop(boxes)
                heapq.heappop(warehouse)
                res+=1
            elif boxes[0]>warehouse[0]:
                heapq.heappop(warehouse)
        return res
                
        
sol=Solution()
sol.maxBoxesInWarehouse([4,5,6,2],
[3,2,6,3,3,7])