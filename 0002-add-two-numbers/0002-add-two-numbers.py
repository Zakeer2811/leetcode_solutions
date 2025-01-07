# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        str1 = ""
        str2 = ""
        
        while temp1 != None:
            str1 += str(temp1.val)
            temp1 = temp1.next
            
        while temp2 != None:
            str2 += str(temp2.val)
            temp2 = temp2.next
            
        n1 = int(str1[::-1])
        n2 = int(str2[::-1])
        total_sum = n1 + n2
        sum_str = str(total_sum)[::-1]
        
        head = ListNode(int(sum_str[0]))
        temp3 = head
        
        for i in range(1, len(sum_str)):
            new_node = ListNode(int(sum_str[i]))
            new_node.next = None
            temp3.next = new_node
            temp3 = temp3.next
            
        return head
