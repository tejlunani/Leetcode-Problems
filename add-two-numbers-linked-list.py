# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        carryo = 0
        ret = ListNode(None)
        dummy = ret

        while l1 or l2 or carryo != 0 :
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carryo

            carryo = sum //10
            sum = sum %10

            ret.next = ListNode(sum)
            ret = ret.next
            sum = 0
            
        return dummy.next
