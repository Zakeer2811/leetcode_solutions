class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def sum_of_subarray_mins(arr):
            # Previous Smaller or Equal Element
            def find_prev_smaller_equal():
                psee, stack = [], []
                for i in range(len(arr)):
                    while stack and arr[stack[-1]] > arr[i]:
                        stack.pop()
                    psee.append(stack[-1] if stack else -1)
                    stack.append(i)
                return psee

            # Next Smaller Element
            def find_next_smaller():
                nse, stack = [], []
                for i in range(len(arr)-1, -1, -1):
                    while stack and arr[stack[-1]] >= arr[i]:
                        stack.pop()
                    nse.append(stack[-1] if stack else len(arr))
                    stack.append(i)
                return nse[::-1]

            prev = find_prev_smaller_equal()
            next_ = find_next_smaller()
            total = 0
            for i in range(len(arr)):
                left = i - prev[i]
                right = next_[i] - i
                total += arr[i] * left * right
            return total

        def sum_of_subarray_maxs(arr):
            # Previous Greater or Equal Element
            def find_prev_greater_equal():
                pgee, stack = [], []
                for i in range(len(arr)):
                    while stack and arr[stack[-1]] < arr[i]:
                        stack.pop()
                    pgee.append(stack[-1] if stack else -1)
                    stack.append(i)
                return pgee

            # Next Greater Element
            def find_next_greater():
                nge, stack = [], []
                for i in range(len(arr)-1, -1, -1):
                    while stack and arr[stack[-1]] <= arr[i]:
                        stack.pop()
                    nge.append(stack[-1] if stack else len(arr))
                    stack.append(i)
                return nge[::-1]

            prev = find_prev_greater_equal()
            next_ = find_next_greater()
            total = 0
            for i in range(len(arr)):
                left = i - prev[i]
                right = next_[i] - i
                total += arr[i] * left * right
            return total

        # Apply formula
        return sum_of_subarray_maxs(nums) - sum_of_subarray_mins(nums)
