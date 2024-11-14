from typing import Optional

# ListNodeクラスの定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ダミーノードを使って、新しいリンクリストの先頭を管理
        dummy = ListNode()
        current = dummy

        # list1とlist2をノードごとに比較しながらマージ
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 残りの要素を追加
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # ダミーノードの次のノードがマージされたリストの先頭
        return dummy.next


# リストからリンクリストを作成するヘルパー関数
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# リンクリストを表示するためのヘルパー関数
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print("[" + ",".join(values) + "]")

# 使用例
solution = Solution()
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

merged_list = solution.mergeTwoLists(list1, list2)
print_linked_list(merged_list)