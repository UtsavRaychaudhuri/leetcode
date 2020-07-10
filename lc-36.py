class Solution(object):
    def isValidSudoku(self, arr):
        row_dict={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        col_dict={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        three_by_three={"00":[],"01":[],"02":[],"10":[],"11":[],"12":[],"20":[],"21":[],"22":[]}
        for i,v in enumerate(arr):
            for  index,j in enumerate(v):
                if j!=".":
                    row_dict[i].append(j)
                    col_dict[index].append(j)
                    keytosearch = str(int(i/3))+str(int(index/3))
                    three_by_three[keytosearch].append(j)
        for (k,v),(k2,v2),(k3,v3) in zip(row_dict.items(),col_dict.items(),three_by_three.items()):
            if len(v)!=len(set(v)) or len(v2)!=len(set(v2)) or len(v3)!=len(set(v3)):
                return False
        return True