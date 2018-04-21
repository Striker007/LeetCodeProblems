class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        for position in range(0,len(strs[0])):
            for i in strs[1:]:
                if position > len(i)-1 or strs[0][position] != i[position]:
                    return strs[0][0:position]

        return strs[0]
