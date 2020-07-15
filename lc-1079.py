class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        self.my_set=set()
        def backtrack(n,my_str,my_arr,combinations):
            if n>=0:
                self.my_set.add(my_str)
            for i in range(len(my_arr)):
                if i in combinations:
                    continue
                elif n+1<=len(my_arr):
                    backtrack(n+1,my_str+my_arr[i],my_arr,combinations|{i})
                else:
                    return
        backtrack(-1,"",list(tiles),set())
        return(len(self.my_set))

sol=Solution()
sol.numTilePossibilities("AAABBC")
                