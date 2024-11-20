class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b_a = int(a,2)
        b_b = int(b,2)
        result = b_a + b_b
        
        return bin(result)[2:]
        
solution = Solution()

print(solution.addBinary("11","1"))