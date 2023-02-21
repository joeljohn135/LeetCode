class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_c={}
        for char in s:
            if char in char_c:
                char_c[char]+=1
            else:
                char_c[char]=1
        for i in range(len(s)):
            if char_c[s[i]]==1:
                return i
        return -1
