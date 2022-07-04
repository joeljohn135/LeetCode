class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<=2):
            return n
        x=0
        y=1
        z=2
        while (n>2):
            x=y
            y=z
            z=x+y
            n=n-1
        return z
            
           
