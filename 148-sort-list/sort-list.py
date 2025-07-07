# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        # Base case: list is empty or has one node
        if not head or not head.next:
            return head

        # Split the list into two halves using slow and fast pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # Cut the list

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Attach the remaining part
        current.next = l1 if l1 else l2
        return dummy.next

        