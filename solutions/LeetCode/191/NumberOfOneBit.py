class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = bin(n)[2:]
        return binary_str.count('1')
            
solutoin = Solution()

print(solutoin.hammingWeight(114514))