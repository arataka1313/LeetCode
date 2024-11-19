class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split(' ')
        filtered_word = [s for s in word if s.strip()]  # 空白文字だけの要素を削除
        return len(filtered_word[-1])

solution = Solution()

print(solution.lengthOfLastWord(" fly me to the moon      "))