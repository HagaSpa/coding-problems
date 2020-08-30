# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        1. Save the next element to tmp.
        2. Set the previous elemennt to head.next. In the first loop, the previous element is NULL.
        3. Set the current element to prev. In the secou¥nd loop, the current element will be the previous element.
        4. Get the next element from tmp.
        """
        tmp = None  # next element
        prev = None # previous element
        while head != None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        # ans = prev.next
        return ans


# Entry point for debug
if __name__ == "__main__":
    li = [1,2,3,4,5]
    root = ListNode()
    head = root
    for l in li:
        head.val = l
        head.next = ListNode()
        head = head.next
    s = Solution()
    s.reverseList(head=root)