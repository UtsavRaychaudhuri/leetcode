class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.first=True
        self.my_arr=list(characters)
        self.my_val=[]
        for i in range(combinationLength):
            self.my_val.append(i)
        

    def next(self):
        """
        :rtype: str
        """
        if self.first:
            self.first=False
            return_arr=""
            for i in self.my_val:
                return_arr+=self.my_arr[i]
            return return_arr
        if self.my_val[-1]==len(self.my_arr)-1:
            for i in range(len(self.my_val)-1,-1,-1):
                if self.my_val[i]<len(self.my_arr)-1:
                    self.my_val[i]+=1
                    break
            for j in range(i+1,len(self.my_val)):
                self.my_val[j]=self.my_val[j-1]+1
        else:
            self.my_val[-1]+=1
        return_arr=""
        for i in self.my_val:
            return_arr+=self.my_arr[i]
        return return_arr
        
        
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.my_val[-1]==len(self.my_arr)-1:
            for i in range(len(self.my_val)-1,-1,-1):
                if self.my_val[i]<len(self.my_arr)-1:
                    break
            for j in range(i,len(self.my_val)):
                k=1
                if self.my_val[j]+k>=len(self.my_arr)-1:
                    return False
                k+=1
            return True
        else:
            return True
                
        


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abc", 2)
param_1 = obj.next()
param_2 = obj.hasNext()
print(param_1)
print(param_2)
print(obj.next())
print(obj.hasNext())
print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.hasNext())
print(obj.hasNext())
print(obj.hasNext())