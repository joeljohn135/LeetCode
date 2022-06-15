class Solution(object):
    
  def romanToInt(self, s):
        dicti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        previous = 0
        sum = 0
        for i in s[::-1]:
            current = dicti[i]
            if previous > current:
                sum -= current
            else:
                sum += current
            prev = current
        return sum
