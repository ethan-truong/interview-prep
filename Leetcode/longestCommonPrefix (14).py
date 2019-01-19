class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        rtn = ""

        smallest = min(strs, key=len)

        for i in range(len(smallest)):
            l = strs[0][i]
            for word in strs:
                if not word[i] == l:
                    return rtn
            rtn += l

        return rtn