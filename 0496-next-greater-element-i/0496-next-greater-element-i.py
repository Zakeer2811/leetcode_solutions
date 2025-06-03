from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        # Key: number in nums2, Value: next greater number to its right (or -1 if none)
        nge_map = {}
        
        # Stack to keep track of potential "next greater elements"
        # This helps us efficiently find the next greater element in O(n) time
        stack = []

        # Traverse the nums2 list from right to left
        # We're processing elements in reverse order so we can use the stack
        # to keep track of greater elements on the right side
        for num in reversed(nums2):
            # Pop elements from the stack that are less than or equal to the current number
            # Because they cannot be the "next greater element" for this number or any number before it
            while stack and stack[-1] <= num:
                stack.pop()

            # If the stack is empty after popping, there is no greater element to the right
            # So we map this number to -1
            if not stack:
                nge_map[num] = -1
            else:
                # Otherwise, the top of the stack is the next greater element
                nge_map[num] = stack[-1]

            # Push the current number onto the stack for future comparisons
            stack.append(num)

        # Now, build the result list for nums1 by looking up the next greater element
        # from the precomputed nge_map dictionary
        result = [nge_map[num] for num in nums1]

        # Return the final result
        return result
