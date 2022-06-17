class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        for i in range(len(strs[0])):
            wrd=strs[0][i]
            for sub in strs:
               if i>len(sub)-1 or wrd!=sub[i]:
                 return strs[0][:i]
        return strs[0]
        
    
