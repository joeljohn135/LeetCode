#Not the best solution requires optimization
class Solution(object):
    def isHappy(self, n):
        
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while n!=1 and i<50:
            quo=0
            while n!=0:
                quo+=(n%10)**2
                n//=10
                i+=1
            n=quo
        return n==1
