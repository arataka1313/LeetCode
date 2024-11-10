class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:   #負の数は除去
            return False

        reversed_num = 0    
        temp = x

        while temp != 0:
            digit = temp % 10   #1桁目の値を代入
            reversed_num = reversed_num * 10 + digit    #reversed_numに1桁ずつ値を入れていく
            temp //= 10     #1桁目を除外した数(12)を求める

        return reversed_num == x
        
solution = Solution()

print(solution.isPalindrome(121))