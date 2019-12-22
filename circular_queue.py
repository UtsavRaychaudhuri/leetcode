
class UtsavCircularQueue(object):
    def __init__(self,k):
        self.k=k
        self.array=[None]*k
        self.tail=self.head=0
        self.firstime=True

    def enqueue(self,number):
        if self.firstime:
            self.array[self.tail]=number
            self.tail+=1
            self.firstime=False
            return self.array
        elif self.tail==self.head:
            return False
        else:
            self.array[self.tail]=number
            if self.tail+1==self.k:
                self.tail=0
            else:
                self.tail+=1
            return self.array
    def dequeue(self):
        if self.array[self.head]==None:
            return False
        self.array[self.head]=None
        self.head+=1
        return self.array



        

        

sol=UtsavCircularQueue(4)
print(sol.enqueue(1))
print(sol.enqueue(2))
print(sol.enqueue(2))
print(sol.enqueue(2))
print(sol.dequeue())

        
