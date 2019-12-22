class MyQueue(object):
    array=[1,2,3]
    def EnQueue(self,a):
        self.array.append(a)
        return self.array
    def Dequeue(self):
        if self.array is None:
            return "Not possible to pop from an empty queue"
        self.array.pop(0)
        return self.array

sol=MyQueue()
print(sol.EnQueue(4))
print(sol.Dequeue())


    

        
        




