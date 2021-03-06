class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        N = len(nums)
        mid = N / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert(nums[:mid],target)
        else:
            result = self.searchInsert(nums[mid+1:],target)
            return result + mid + 1
                
        #Using Binary Search 
