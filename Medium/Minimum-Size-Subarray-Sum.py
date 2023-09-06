class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        sum = 0
        left = 0  
        right = 0  
        shortest = float('inf')          
        while right < n:
            sum += nums[right] 
            while sum >= target:  
                sum -= nums[left]
                left += 1
                shortest = min(shortest, right - left + 2) 
            right += 1
        return shortest if shortest != float('inf') else 0
