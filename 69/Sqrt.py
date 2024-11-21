import numpy as np

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(np.sqrt(x))
    
solution = Solution()

print(solution.mySqrt(4))