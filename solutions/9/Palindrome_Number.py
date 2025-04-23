class Solution:
    def isPalindrome(self, x: int) -> bool:
        xlist = [digit for digit in str(x)]  #xをリストとして取得
        
        flag = 0 #True
        n = len(xlist)
        for i in range(n):
            if xlist[i] != xlist [n - i - 1]: #リストの前後を比較していく
                flag = 1

        if flag == 0:
            return True
        else:
            return False
        
solution = Solution()

print(solution.isPalindrome(121))