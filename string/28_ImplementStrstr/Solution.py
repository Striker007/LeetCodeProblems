class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "" or needle == haystack:
            return 0

        if len(needle) > len(haystack):
            return -1

        # check first and last letters equality
        if len(needle) == len(haystack) and not \
           (haystack[0] == needle[0] and haystack[-1:] == needle[-1:]):
                return -1

        for i in range(len(haystack)):  
            # check all needle letters from position in haystack
            for j in range(len(needle)):
                if i+j < len(haystack) and haystack[i+j] != needle[j]:
                    break
                # if we here and it's the last letter of a needle then the search is successful
                if j == len(needle) - 1 and (len(haystack) - i) >= len(needle):
                    return i

        return -1

