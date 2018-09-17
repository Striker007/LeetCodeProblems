class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for l in s:
            if l not in letters:
                letters[l] = 0
            letters[l] += 1
        
        sum = 0
        for i in letters:
            sum += letters[i] // 2 * 2
            if sum % 2 == 0 and letters[i] % 2 == 1:
                sum += 1
        return sum