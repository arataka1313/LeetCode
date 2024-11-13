class Solution:
    def isValid(self, s: str) -> bool:
        n_p = 0
        n_sb = 0
        n_cb = 0
        for i in range(len(s)):            
            if s[i] == '(':
                n_p += 1    
            if s[i] == '[':
                n_sb += 1   
            if s[i] == '{':
                n_cb += 1   
            if s[i] == ')':
                n_p -= 1    
            if s[i] == ']':
                n_sb -= 1  
            if s[i] == '}':
                n_cb -= 1   
        if n_p == 0 and n_sb == 0 and n_cb == 0:
            return True
        else:
            return False

solution = Solution()

print(solution.isValid("{{[()]}}"))