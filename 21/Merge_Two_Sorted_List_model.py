from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            
            cur = cur.next
            
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
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