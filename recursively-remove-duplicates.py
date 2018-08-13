# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            curr = head.next
            while head.val == curr.val:
                curr = curr.next
            head.next = curr
            
            self.deleteDuplicates(curr)
            return head
