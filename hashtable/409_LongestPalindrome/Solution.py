class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        center = ""
        word_left = ""
        word_right = ""

        repeat = 0
        prev = ""

        for letter in s:
            if letter == prev:
                repeat += 1
            else:
                if repeat > 1:
                    word_left += (repeat//2 * prev)
                    word_right += (repeat//2 * prev)
                if repeat % 2 != 0:
                    center = prev
                prev = letter
                repeat = 0

        return len(word_left + center + word_right)
