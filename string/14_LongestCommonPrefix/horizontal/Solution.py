class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            print(i)
            while(prefix not in strs[i][0:len(prefix)]):
                print(prefix)
                prefix = prefix[0: len(prefix) - 1]
                if (prefix == ""):
                    return "";
        return prefix
