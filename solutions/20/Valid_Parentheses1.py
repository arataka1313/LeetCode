class Solution:
    def isValid(self, s: str) -> bool:
        # 括弧の対応関係を辞書で定義
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # 閉じ括弧の場合
            if char in bracket_map:
                # スタックが空でないかつ、トップにある要素が対応する開き括弧でなければFalse
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # 開き括弧ならスタックに追加
                stack.append(char)

        # 全ての括弧がペアになっていればスタックは空
        return not stack

solution = Solution()
print(solution.isValid("()[]([])"))
