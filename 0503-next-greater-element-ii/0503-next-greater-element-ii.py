class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n  # Initialize the result array with -1 (default value if no greater element exists)
        stack = []  # Stack to keep the next greater elements (monotonically decreasing)

        # Loop from 2n - 1 down to 0 to simulate circular array (we go through the array twice)
        for i in range(2 * n - 1, -1, -1):
            # Current index in circular array: i % n

            # Pop elements from the stack that are less than or equal to the current element,
            # because they can't be the next greater for this or any previous element.
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            # For the first pass (i < n), we update the result
            if i < n:
                if not stack:
                    nge[i] = -1  # No next greater element found
                else:
                    nge[i] = stack[-1]  # The top element on the stack is the next greater

            # Push the current element onto the stack for future comparisons
            stack.append(nums[i % n])

        return nge
