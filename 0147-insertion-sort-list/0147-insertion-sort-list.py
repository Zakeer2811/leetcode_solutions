# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        curr = head.next

        while curr:
            if prev.val <= curr.val:
                prev = curr
                curr = curr.next
                continue

            thead = dummy
            while thead.next and thead.next.val < curr.val:
                thead = thead.next

            prev.next = curr.next
            curr.next = thead.next
            thead.next = curr
            curr = prev.next

        return dummy.next
