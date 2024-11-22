class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)  #dp[i]は1と2を使ってiを表現する方法の数を表す
        
        dp[0] = 1   #初期条件
        
        #動的計画法
        for i in range(1,n + 1):
            dp[i] = dp[i - 1]
            if i >= 2:
                dp[i] += dp[i - 2]
        
        return dp[n]
        
solution = Solution()

print(solution.climbStairs(8))