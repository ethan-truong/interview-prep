# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None

        rtn = ListNode(0)
        curr = rtn

        while l1 is not None or l2 is not None:
            if l1 is None:
                curr.next = l2
                break
            elif l2 is None:
                curr.next = l1
                break
            elif l1.val > l2.val:
                curr.next = ListNode(l2.val)
                l2 = l2.next
                curr = curr.next
            else:
                curr.next = ListNode(l1.val)
                l1 = l1.next
                curr = curr.next

        return rtn.next
