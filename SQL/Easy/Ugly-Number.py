class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n!=0:
            if n%2==0:
                n=n/2
            elif n%3==0:
                n=n/3
            elif n%5==0:
                n=n/5
            elif n==1:
                return True
            else:
                return False

