class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, G: list[int]) -> int:
        # Step 1: Convert the list G into a set for O(1) lookups
        G_set = set(G)
        
        # Initialize the result counter
        res = 0
        
        # Step 2: Traverse the linked list
        cur = head
        while cur:
            # Step 3: Check if the current node is in the set and it is the start of a new component
            if cur.val in G_set and (cur.next is None or cur.next.val not in G_set):
                res += 1
            cur = cur.next
        
        return res
