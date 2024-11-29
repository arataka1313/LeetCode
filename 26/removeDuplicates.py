from collections import Counter
from typing import List

# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        #ポインタを使って重複を削除
        unique_index = 0    #重複なしの位置を管理
        
        for i in range(1,len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        
        return unique_index + 1
                            
solutoin = Solution()

print(solutoin.removeDuplicates([1,1,2]))