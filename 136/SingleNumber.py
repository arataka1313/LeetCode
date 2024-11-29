from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 要素の出現回数をカウント
        counts = Counter(nums)
        for num, count in counts.items():
            if count == 1:
                return num
        return None  # ユニークな要素がない場合
            
solutoin = Solution()

print(solutoin.singleNumber([1,1,4,5,1,4]))