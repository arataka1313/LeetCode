class Solution:
    def romanToInt(self, s: str) -> int:
        # ローマ数字の対応表
        roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        total = 0
        prev_value = 0

        # ローマ数字の文字を左から右に処理
        for char in s:
            value = roman_to_int_map[char]  # 対応する値を取得

            # 現在の値が前の値より小さければ減算
            if value > prev_value:
                total += value - 2 * prev_value  # 引き算部分を補正
            else:
                total += value

            prev_value = value  # 前の値を更新

        return total

solution = Solution()

print(solution.romanToInt('MCMXCIV'))