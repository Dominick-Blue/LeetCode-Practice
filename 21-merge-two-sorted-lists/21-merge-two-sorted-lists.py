# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy_head = ListNode(None)
        tail = dummy_head
        curr1 = list1
        curr2 = list2
        
        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            
            tail = tail.next
        
        if curr1 is not None: tail.next = curr1
        if curr2 is not None: tail.next = curr2
        
        return dummy_head.next