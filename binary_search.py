class Utsav(object):
    def Binary_search(self,l,m,h,a,search_term):
        if a[m]==search_term:
            return m
        elif a[m]>search_term:
            return self.Binary_search(l,int((l+h)/2),m-1,a,search_term)
        else:
            return self.Binary_search(m+1,int((m+1+h)/2),h,a,search_term)

    def Solution(self):
        a=[1,2,3,4,5,6,7,8]
        l=0
        h=len(a)-1
        m=int((l+h)/2)
        return self.Binary_search(l,m,h,a,4)

my_obj=Utsav()
print(my_obj.Solution())