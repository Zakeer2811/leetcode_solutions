# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        l.sort()
        temp=head
        for i in range(len(l)):
            temp.val=l[i]
            temp=temp.next
        return head