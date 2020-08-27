# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        a = ListNode(0)
        p = a
        s = set() # 重複した値を入れておく
        
        while head:
            # 重複した値がいくつあるのか不明だからsに含まれていたらすでに重複とみなす。
            # 連結リストは現在 or 次の要素しか調べられず、前の要素がいくつだったのかわかんないから
            if (head.next and head.val == head.next.val) or head.val in s:
                s.add(head.val)
                head = head.next
            else:
                a.next = head
                a = a.next
                head = head.next
        a.next = None
        return p.next