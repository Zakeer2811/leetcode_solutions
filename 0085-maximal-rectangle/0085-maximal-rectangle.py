class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            # Add a sentinel 0 height at the end to force processing all bars in the stack
            heights.append(0)
            stack = []  # Monotonic increasing stack (stores indices)
            max_area = 0

            for i, h in enumerate(heights):
                # While the current bar is shorter than the top of the stack, process the taller bars
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]  # The bar being processed (taller one)

                    # Width is determined by current index and index on top of stack after popping
                    # If stack is empty, it means the popped bar was the smallest so far
                    width = i if not stack else i - stack[-1] - 1

                    # Area = height * width, using current height as smallest bar
                    area = height * width
                    max_area = max(max_area, area)

                # Push current index to stack (ensuring increasing order of heights)
                stack.append(i)

            return max_area

        # Edge case: if matrix is empty, return 0
        if not matrix or not matrix[0]:
            return 0

        rowslen = len(matrix)
        columnslen = len(matrix[0])

        # This will store the histogram heights (prefix sums of '1's column-wise)
        prefixsum = [[0] * columnslen for _ in range(rowslen)]

        # Build prefixsum for row 0: copy the first row (convert '1' to int)
        for j in range(columnslen):
            prefixsum[0][j] = int(matrix[0][j])

        # Build prefixsum for the remaining rows:
        # If the current cell is '1', add 1 to the value above to keep histogram
        # Otherwise, reset to 0 (as the histogram is broken)
        for i in range(1, rowslen):
            for j in range(columnslen):
                prefixsum[i][j] = prefixsum[i - 1][j] + 1 if matrix[i][j] == '1' else 0

        MaxArea = 0  # Initialize the maximum rectangle area

        # For each row (treated as histogram), calculate the largest rectangle area
        for i in range(rowslen):
            MaxArea = max(MaxArea, largestRectangleArea(prefixsum[i]))

        return MaxArea

    
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     n = len(heights)

    #     # Function to find the index of the Next Smaller Element (NSE) to the right
    #     def next_smaller_elements():
    #         stack = []
    #         nse = [n] * n  # Initialize with 'n', i.e., end of histogram (virtual boundary)
    #         for i in range(n - 1, -1, -1):
    #             # Maintain monotonic increasing stack
    #             while stack and heights[stack[-1]] >= heights[i]:
    #                 stack.pop()
    #             # If stack is not empty, top element is index of next smaller element
    #             if stack:
    #                 nse[i] = stack[-1]
    #             stack.append(i)
    #         return nse

    #     # Function to find the index of the Previous Smaller Element (PSE) to the left
    #     def prev_smaller_elements():
    #         stack = []
    #         pse = [-1] * n  # Initialize with -1, i.e., start of histogram (virtual boundary)
    #         for i in range(n):
    #             # Maintain monotonic increasing stack
    #             while stack and heights[stack[-1]] >= heights[i]:
    #                 stack.pop()
    #             # If stack is not empty, top element is index of previous smaller element
    #             if stack:
    #                 pse[i] = stack[-1]
    #             stack.append(i)
    #         return pse

    #     # Get PSE and NSE arrays
    #     next_smaller = next_smaller_elements()
    #     prev_smaller = prev_smaller_elements()

    #     max_area = 0

    #     # Now calculate the maximum rectangular area for each bar
    #     for i in range(n):
    #         height = heights[i]
    #         left = prev_smaller[i]     # Index of previous smaller bar
    #         right = next_smaller[i]    # Index of next smaller bar

    #         # ✅ WHY THIS FORMULA WORKS:
    #         # The current bar at index i is the **smallest** in its range of influence.
    #         # From left+1 to right-1 (both inclusive) — all bars are **greater or equal** to height[i].
    #         # So we can form a rectangle of height = height[i] and width = (right - left - 1)
    #         width = right - left - 1
    #         area = height * width
    #         max_area = max(max_area, area)

    #     return max_area
       