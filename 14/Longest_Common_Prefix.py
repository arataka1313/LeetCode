from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""   #strsが空だったら空文字列を返す
        
        prefix = strs[0]    #最初の文字列を初期の共通接頭辞prefixにする
        
        #リスト2番目以降の文字列について順に共通接頭辞を確認
        for strs in strs[1:]:
            #strsの先頭がprefixと一致しないとき順に共通接頭辞を確認
            while not strs.startswith(prefix):
                prefix = prefix[:-1]  # 接頭辞を1文字ずつ短縮
                if prefix == "":
                    break
        return prefix
            
solution = Solution()

strs = ["cat","cancer","car"]
print(solution.longestCommonPrefix(strs))