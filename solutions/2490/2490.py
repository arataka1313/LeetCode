class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)   #文字列の個数を格納
        
        #最初の文字列の先頭と最後尾の文字列の最後を比較
        if sentence[0] != sentence[n-1]:
            return False

        for i in range(1, n-1):     #最初の文字と最後の文字を除いた文字列を頭の方から走査
            if sentence[i] == ' ':      #もしその文字が空白(スペース)文字だったら(英文の切れ目はスペースだから)
                if sentence[i-1] != sentence[i+1]:  #その空白文字の前後の文字が違かったら循環文ではない
                    return False
                    
        return True
    
solution = Solution()

print(solution.isCircularSentence("a a ba"))