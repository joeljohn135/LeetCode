class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in digits:
            number = i + number*10
        number += 1
        str_number = str(number)
        lists = []
        for digit in str_number:
            lists.append(str_number)
        return lists[0]
         
