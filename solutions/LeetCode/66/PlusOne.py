from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            num = int("".join(map(str, digits)))
            num += 1
            return [int(digit) for digit in str(num)]
solution = Solution()

print(solution.plusOne([1,3,9,9]))