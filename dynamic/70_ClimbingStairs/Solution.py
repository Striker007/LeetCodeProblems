class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 3:
            return n

        _prev2 = 0
        _prev1 = 1

        for i in range(1, n + 1):

            if i == n:
                return _prev2 + _prev1
            
            z = _prev2
            _prev2 = _prev1
            _prev1 = _prev2 + z


        return 0

    
class Solution2:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        variants = [1,2]
        if n>2:
            for i in range(3, n + 1):
                variants.append(variants[i-2] + variants[i-3])
            return variants[-1]
        else:
            return variants[n-1]
    
