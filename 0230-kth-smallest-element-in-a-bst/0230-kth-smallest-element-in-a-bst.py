class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        
        while True:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the node from the stack (current node is the smallest unprocessed node)
            current = stack.pop()
            k -= 1
            
            # If k is 0, return the value of the k-th smallest node
            if k == 0:
                return current.val
            
            # Move to the right child
            current = current.right
