from typing import List
import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            if target in nums:
                return nums.index(target)
            else:
                bisect.insort(nums, target)
                return nums.index(target)
        
solution = Solution()

print(solution.searchInsert([1,3,5,6],4))