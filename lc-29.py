class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a, b = abs(dividend), abs(divisor)
        neg = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0 #sign
        origdiv = b
        
        ans = 0
        while a >= origdiv:
            cur = 1
            while a >= (b << 1):
                b <<= 1
                cur <<= 1

            a -= b # update long division
            b = origdiv # reset
            ans += cur

        ans = -ans if neg else ans
        #print(ans)
        INT_MAX = 2147483647 # check overflow
        if ans > INT_MAX:
            ans = INT_MAX
        if ans < -INT_MAX - 1:
            ans = -INT_MAX - 1
        return ans
            