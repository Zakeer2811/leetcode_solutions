class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = ''             # Final result string (will be built in reverse)
        stack = []           # Stack to store digits of the resulting smallest number

        # Step 1: Process each digit in the number
        for digit in num:
            # Remove digits from the stack if they are larger than the current digit
            # and we still have digits to remove (k > 0)
            while stack and stack[-1] > digit and k > 0:
                stack.pop()  # Remove the larger digit
                k -= 1       # One removal done

            # Add current digit to the stack
            stack.append(digit)

        # Step 2: If there are still removals left, remove from the end
        while k:
            stack.pop()
            k -= 1

        # Step 3: If stack is empty after all removals, return "0"
        if not stack:
            return "0"

        # Step 4: Build the final number from the stack
        while stack:
            res += stack.pop()  # Pop to build reversed number

        # Step 5: Remove any trailing zeros (which are actually leading zeros after reversal)
        res = res.rstrip('0')

        # Step 6: Return the result reversed back to correct order
        return res[::-1] if res else "0"
