class Solution(object):
    def isPalindrome(self, x):
        temp=x
        rev=0
        while temp>0:
            rem=temp%10
            rev = (rev*10)+rem
            temp=temp//10
        if x == rev:
            return 1
        else:
            return 0
