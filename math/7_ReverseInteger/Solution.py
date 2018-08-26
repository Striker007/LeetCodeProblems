class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:    
            sign = -1

        x = abs(x)
        x_rev = 0
        while x > 0:
            pop = x % 10
            x_rev = x_rev * 10 + pop
            x = x // 10

        # alternatively
        # compare positive number with 0x7fffffff
        # compare size x_rev.bit_length() > 31
        if x_rev > 2**31-1  or x_rev < -2**31:
            return 0

        return x_rev * sign