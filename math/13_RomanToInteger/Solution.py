class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0
        prev = ""
        for l in s:

            if (prev == "I" and l in ["V", "X"]) or \
                (prev == "X" and l in ["L", "C"]) or \
                (prev == "C" and l in ["D", "M"]):
                    
                num = num + (roman[l] - (roman[prev] * 2))

            else:
                num = num + roman[l]
            
            prev = l

        return num
