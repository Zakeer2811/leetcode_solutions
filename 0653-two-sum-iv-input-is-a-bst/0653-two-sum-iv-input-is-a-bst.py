class Solution:
    def findTarget(self, root, k):
        # If tree is empty, there's no way to find any pair
        if not root:
            return False

        # These stacks will simulate two iterators:
        # 1. In-order (smallest to largest)
        # 2. Reverse in-order (largest to smallest)
        left_stack = []   # to go from smallest to largest
        right_stack = []  # to go from largest to smallest

        # Helper function to push all the leftmost nodes into left_stack
        # This initializes our in-order traversal (smallest element first)
        def push_left(node):
            while node:
                left_stack.append(node)
                node = node.left  # Keep going left

        # Helper function to push all the rightmost nodes into right_stack
        # This initializes our reverse in-order traversal (largest element first)
        def push_right(node):
            while node:
                right_stack.append(node)
                node = node.right  # Keep going right

        # Moves the in-order pointer (left side) forward to the next smallest element
        def get_next():
            # Pop the top node which is the current smallest unvisited node
            node = left_stack.pop()
            # After visiting this node, we must check its right subtree
            # and go all the way left again to find the next smallest
            push_left(node.right)
            return node.val

        # Moves the reverse in-order pointer (right side) backward to the next largest element
        def get_prev():
            # Pop the top node which is the current largest unvisited node
            node = right_stack.pop()
            # After visiting this node, we must check its left subtree
            # and go all the way right to find the next largest
            push_right(node.left)
            return node.val

        # Step 1: Initialize both stacks
        push_left(root)   # Initialize left_stack with smallest path
        push_right(root)  # Initialize right_stack with largest path

        # Step 2: Get the initial smallest and largest values
        left = get_next()     # smallest value in BST
        right = get_prev()    # largest value in BST

        # Step 3: Apply two-pointer approach just like on a sorted array
        while left < right:
            total = left + right  # Sum of current two values
            if total == k:
                return True       # Found two elements whose sum is k
            elif total < k:
                left = get_next() # We need a bigger sum, move the left pointer forward
            else:
                right = get_prev() # We need a smaller sum, move the right pointer backward

        # If the loop ends, no such pair exists
        return False
'''
This solution simulates two pointers (like you would use in a sorted array) directly on the Binary Search Tree (BST) using two stacks:

left_stack tracks the next smallest node.

right_stack tracks the next largest node.

You keep checking if the sum of two nodes is equal to k, and move the pointers inward until they meet or you find the answer.
'''