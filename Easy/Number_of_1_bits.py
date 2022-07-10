class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        while n > 0:
            n, rem = divmod(n,2)
            if rem == 1:
                 k+= 1
        return k
