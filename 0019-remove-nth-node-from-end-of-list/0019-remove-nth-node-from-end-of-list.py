# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge case: if the list has 0 or 1 node, removing any node means returning None
        if not head or not head.next:
            return None
        
        # Create a dummy node pointing to head to simplify edge case (e.g. deleting head itself)
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers at dummy
        fast = slow = dummy
        
        # Step 1: Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Step 2: Move both fast and slow one step at a time
        # Stop when fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Step 3: slow is just before the node to delete
        # Bypass the target node
        slow.next = slow.next.next
        
        # Return the updated list, starting from dummy.next
        return dummy.next if dummy.next else None

# -------------------------------------------------------------------
# ✅ INTUITION:

"""
To remove the nth node from the end in one pass, we use the **two-pointer technique**:

1. Start both `fast` and `slow` at a dummy node before the head.
2. Move `fast` pointer `n` steps ahead — this creates a gap of `n` nodes between `fast` and `slow`.
3. Now move both pointers one step at a time. When `fast` reaches the last node, `slow` is just before the target node to remove.
4. Delete that node by setting `slow.next = slow.next.next`.

\U0001f3af Why it works:
- The `n`-step gap ensures that when `fast` is at the end, `slow` is exactly at the right position (length - n).
- Using a dummy node helps even when the node to remove is the head.

This approach ensures a **single traversal (O(n))** and **no extra space (O(1))**.
"""

# -------------------------------------------------------------------
# \U0001f501 DRY RUN:

# Input: head = [1, 2, 3, 4, 5], n = 2
# Expected Output: [1, 2, 3, 5]

# Step-by-step:

# Initial list:
# dummy -> 1 -> 2 -> 3 -> 4 -> 5
# fast and slow both at dummy

# Step 1: Move fast 2 steps:
# fast -> 1
# fast -> 2

# Step 2: Move both fast and slow until fast.next is None:
# fast -> 3, slow -> 1
# fast -> 4, slow -> 2
# fast -> 5, slow -> 3

# Step 3: slow is just before node 4
# slow.next = node with value 4
# Remove node 4: slow.next = slow.next.next

# Final list:
# dummy -> 1 -> 2 -> 3 -> 5
# Return dummy.next

# Output: [1, 2, 3, 5]
