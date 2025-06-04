class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Helper function to find the index of the Next Smaller Element (NSE) for each element
        def find_next_smaller_indices(arr):
            nse = []
            stack = []  # Monotonic increasing stack to keep indices
            for i in range(len(arr)-1, -1, -1):  # Traverse from right to left
                # Pop elements from stack until we find a smaller element
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                # If no smaller element to the right, store virtual index beyond array length
                if not stack:
                    nse.append(len(arr))
                else:
                    nse.append(stack[-1])  # Store index of next smaller element
                # Push current index onto stack
                stack.append(i)
            return nse[::-1]  # Reverse to match original order

        # Helper function to find the index of the Previous Smaller or Equal Element (PSEE) for each element
        def find_prev_smaller_equal_indices(arr):
            psee = []
            stack = []  # Monotonic increasing stack to keep indices
            for i in range(len(arr)):  # Traverse from left to right
                # Pop elements from stack while they are strictly greater than current
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                # If no smaller or equal element to the left, store -1
                if not stack:
                    psee.append(-1)
                else:
                    psee.append(stack[-1])  # Store index of previous smaller or equal element
                # Push current index onto stack
                stack.append(i)
            return psee

        # Get arrays for Next Smaller Element and Previous Smaller or Equal Element
        next_smaller_indices = find_next_smaller_indices(arr)
        prev_smaller_equal_indices = find_prev_smaller_equal_indices(arr)

        total_sum = 0  # Total contribution of all subarray minimums
        mod = 10**9 + 7  # Use given modulo to prevent overflow

        # Calculate the contribution of each element as the minimum of subarrays
        for i in range(len(arr)):
            # Left span: number of elements between current and previous smaller/equal element
            left = i - prev_smaller_equal_indices[i]

            # Right span: number of elements between current and next smaller element
            right = next_smaller_indices[i] - i

            # Each element contributes to left * right subarrays as the minimum
             # Proper modular addition to avoid integer overflow and match expected output
            total_sum = (total_sum + (left * right * arr[i]) % mod) % mod

        # Return result modulo mod
        return total_sum % mod
