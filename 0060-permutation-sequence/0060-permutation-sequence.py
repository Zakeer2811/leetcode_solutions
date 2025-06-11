from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # --------------------------------------------------------------------------------
        # \U0001f511 Key Idea:
        # --------------------------------------------------------------------------------
        # There are n! total permutations of n numbers.
        # The permutations can be grouped by fixing each digit at the first position.
        #
        # For example, if n = 4, the permutations are:
        # Group 1 (starting with 1) → 6 permutations: 1234, 1243, 1324, ..., 1432
        # Group 2 (starting with 2) → next 6 permutations
        # Group 3 (starting with 3) → next 6
        # Group 4 (starting with 4) → last 6
        #
        # So, for each digit, we can mathematically compute which number should be at
        # that position by dividing k by (n-1)!, then continue for remaining digits.
        # --------------------------------------------------------------------------------

        # List of numbers to build the permutation from
        numbers = [i for i in range(1, n + 1)]

        # (n - 1)! gives the number of permutations for each group of fixed starting digits
        fact = factorial(n - 1)

        # Convert k from 1-based to 0-based index for simpler calculations
        k -= 1

        # This will store the resulting permutation
        ans = ""

        # --------------------------------------------------------------------------------
        # Why use DIVISION and MODULO here?
        # --------------------------------------------------------------------------------
        # Division (k // fact):
        #   - Determines which block/group the k-th permutation falls into.
        #   - Each group corresponds to permutations starting with a particular digit.
        #
        # Modulo (k % fact):
        #   - Updates k to reflect the position inside the chosen group
        #   - Allows us to repeat the process for the remaining digits
        # --------------------------------------------------------------------------------

        # Construct the permutation
        while numbers:
            # Pick the index of the current digit
            index = k // fact
            ans += str(numbers[index])  # Append that digit to result

            # Remove the used digit
            numbers.pop(index)

            # Break early if no numbers left
            if not numbers:
                break

            # Update k to reflect new offset inside the group
            k %= fact

            # Update fact: total permutations for next group (i.e., (n-2)!, (n-3)!, ...)
            fact //= len(numbers)

        return ans

# --------------------------------------------------------------------------------
# \U0001f9ea How It Works Step-by-Step (Example: n = 4, k = 9)
# --------------------------------------------------------------------------------
# Goal: Find the 9th permutation in lexicographic order of [1, 2, 3, 4]
#
# Total permutations = 4! = 24
# Each leading digit has (n-1)! = 3! = 6 permutations
#
# Convert k from 1-based to 0-based: k = 9 - 1 = 8
#
# Step-by-step:
# ------------------------------------------------------------------------------
# 1st Digit:
#   index = 8 // 6 = 1 → Pick 2 (second number in [1, 2, 3, 4])
#   ans = "2"
#   Remove 2 → numbers = [1, 3, 4]
#   k = 8 % 6 = 2
#   fact = 6 // 3 = 2
#
# 2nd Digit:
#   index = 2 // 2 = 1 → Pick 3
#   ans = "23"
#   Remove 3 → numbers = [1, 4]
#   k = 2 % 2 = 0
#   fact = 2 // 2 = 1
#
# 3rd Digit:
#   index = 0 // 1 = 0 → Pick 1
#   ans = "231"
#   Remove 1 → numbers = [4]
#
# 4th Digit:
#   Only one number left → Pick 4
#   ans = "2314"
#
# ✅ Final Output: "2314"
