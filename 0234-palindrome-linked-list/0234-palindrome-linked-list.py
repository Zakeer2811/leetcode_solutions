# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        s=""
        while temp!=None:
            s+=str(temp.val)
            temp=temp.next
        rev=s[::-1]
        return rev==s
            
        