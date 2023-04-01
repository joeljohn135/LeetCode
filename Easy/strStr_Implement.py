class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        n = len(needle)
        prefix_suffix = self.get_prefix_suffix(needle)

        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n:
                    return i - n
            elif j > 0:
                j = prefix_suffix[j-1]
            else:
                i += 1

        return -1

    def get_prefix_suffix(self, needle):
        n = len(needle)
        prefix_suffix = [0] * n

        i, j = 1, 0
        while i < n:
            if needle[i] == needle[j]:
                j += 1
                prefix_suffix[i] = j
                i += 1
            elif j > 0:
                j = prefix_suffix[j-1]
            else:
                prefix_suffix[i] = 0
                i += 1

        return prefix_suffix
