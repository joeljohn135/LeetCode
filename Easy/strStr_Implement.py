class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        h = len(haystack)
        if h < n:
            return -1
        else:
            for i in range(h-n+1):
                if haystack[i:i+n] == needle:
                    return i
            return -1
