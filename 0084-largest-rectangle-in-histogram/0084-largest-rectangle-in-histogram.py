class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Step 1: Find the index of the Next Smaller Element (NSE) to the right for each bar
        def next_smaller_elements():
            stack = []
            nse = [n] * n  # If no smaller element to the right, use 'n' (acts like a virtual zero-height bar)
            for i in range(n - 1, -1, -1):  # Traverse from right to left
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()  # Pop elements taller or equal to current
                if stack:
                    nse[i] = stack[-1]  # Index of the first smaller element to the right
                stack.append(i)
            return nse

        # Step 2: Find the index of the Previous Smaller Element (PSE) to the left for each bar
        def prev_smaller_elements():
            stack = []
            pse = [-1] * n  # If no smaller element to the left, use -1 (acts like a virtual zero-height bar)
            for i in range(n):  # Traverse from left to right
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()  # Pop elements taller or equal to current
                if stack:
                    pse[i] = stack[-1]  # Index of the first smaller element to the left
                stack.append(i)
            return pse

        # Get the NSE and PSE arrays
        next_smaller = next_smaller_elements()
        prev_smaller = prev_smaller_elements()

        max_area = 0

        # Step 3: Compute area for each bar using the formula
        for i in range(n):
            height = heights[i]               # Current bar's height
            left = prev_smaller[i]           # Index of previous smaller bar
            right = next_smaller[i]          # Index of next smaller bar
            width = right - left - 1         # Width of rectangle that can be formed with current bar as smallest

            # \U0001f50d WHY THE FORMULA WORKS:
            # The bar at index `i` is the shortest in the rectangle.
            # - It can extend to the left until the first bar smaller than it → index `left`
            # - It can extend to the right until the first bar smaller than it → index `right`
            # So, the total number of bars it spans = right - left - 1
            # Multiply height * width to get the area of that rectangle
#             For any bar at index i, the largest rectangle where this bar is the smallest in height stretches:

# Left to the first smaller bar before it (prev_smaller[i])

# Right to the first smaller bar after it (next_smaller[i])

# So total span = right - left - 1 (excluding the smaller bars at both ends)

# Multiply this width with the height of the current bar → total area

            area = height * width             # Calculate area with current bar as the shortest
            max_area = max(max_area, area)    # Update max area if this is larger

        return max_area
