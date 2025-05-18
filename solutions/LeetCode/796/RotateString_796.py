class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            shifted_s = s[i:] + s[:i]
            if shifted_s == goal:
                return True
        return False

solution = Solution()

print(solution.rotateString('abcde','deabc'))