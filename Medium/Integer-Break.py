class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = { 1 : 1 }
        def dfs(num):
            if num in dp: 
                return dp[num]
            dp[num] = 0 if num == n else num
            for i in range(1, num): 
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        return dfs(n)
