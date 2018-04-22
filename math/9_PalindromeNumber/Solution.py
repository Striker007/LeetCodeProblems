class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed = 0
        while x > reversed:
            reversed = (reversed * 10) + (x % 10)
            x = x // 10
        return True if reversed == x or reversed // 10 == x else False
