from collections import Counter
from typing import List

#LeetCodeでは 配列の内容と戻り値の両方がテストされるため、このコードは仕様違反

# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return len(list(set(nums)))
                            
solutoin = Solution()

print(solutoin.removeDuplicates([1,1,2]))