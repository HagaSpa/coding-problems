# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        l1とl2を最後まで回して、１つずつ文字列化して、joinする
        """
        l1_v = ""
        while l1 != None:
            l1_v = str(l1.val) + l1_v
            l1 = l1.next
        
        l2_v = ""
        while l2 != None:
            l2_v = str(l2.val) + l2_v
            l2 = l2.next
        
        v = str(int(l1_v) + int(l2_v))
        
        rv = v[::-1]
        ans = ListNode(0)
        head = ans
        for i,v in enumerate(rv):
            head.val = v
            # not last element
            if i != len(rv)-1:
                head.next = ListNode(0)
                head = head.next
        return ans
            
        