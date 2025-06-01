# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=head
        curr=head.next
        while curr:
            if prev.val<=curr.val:
                prev=curr
                curr=curr.next
                continue
            thead=dummy
            while thead.next:
                if thead.next.val>curr.val:
                    break
                thead=thead.next
            prev.next=curr.next
            curr.next=thead.next
            thead.next=curr
            curr=prev.next
        return dummy.next
