class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        reversed = 0    
        while x != 0:
            reversed = (reversed * 10) + (x % 10)
            x = x // 10

        return reversed * sign if reversed < 0x7fffffff else 0
