# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set=set(nums)
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy
        current=head
        while prev.next:
            if prev.next.val in nums_set:
                prev.next=prev.next.next
            else:
                prev=prev.next
        return dummy.next
            
        