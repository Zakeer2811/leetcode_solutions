from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, target_remaining, current_combination, nums, all_combinations):
            # Base case: if target is met, add a copy of the current combination
            if target_remaining == 0:
                all_combinations.append(current_combination[:])
                return

            # Loop through all candidates starting from the current index
            # \U0001f501 Try all candidates starting from the current index
            #
            # \U0001f4cc Why loop from `index` to `len(nums)`?
            # -------------------------------------------------------
            # ➤ At the current step in recursion, try all candidates starting from `index` onward.
            #
            # \U0001f9e0 Reason: To build combinations in non-descending order and avoid duplicates.
            # We're building combinations (not permutations), so the order **within a combination** doesn’t matter.
            #
            # ➤ To avoid generating different permutations of the same combination
            #    (like [1,2] and [2,1]), we only consider candidates **after or at** the current position.
            #
            # ➤ So if we already used candidates[0], we should only consider candidates[1:] next
            #    to keep things in order.
            #
            # \U0001f504 Without index control:
            #    If we looped from 0 every time:
            #       - We'd consider all elements in every recursive call — leading to **duplicate permutations**.
            #       - For example, you’d generate both [1,2] and [2,1] as separate answers — which is invalid.
            #
            # \U0001f501 Why not just loop over all?
            #    Because the problem asks for:
            #       - **combinations**, not permutations.
            #       - **no repeated combinations**, even if input has duplicates.
            #
            # ➤ That’s why we move forward in the list at every step:
            #       backtrack(i + 1, ...)
            #       - This ensures that we don’t reuse the same element.
            #       - And keeps the choices in increasing index order.
            #
            # \U0001f440 Visual Example:
            # Input: candidates = [1, 2, 3], target = 3
            # Start at index 0 → try 1
            # → Then recurse starting at index 1 → try 2
            # → So combination becomes [1, 2], not [2, 1]
            # This ensures only one of [1,2] or [2,1] gets generated — which is correct,
            # because they’re the same combination.
            # -------------------------------------------------------

            for i in range(index, len(nums)):

                # -----------------------------------------------
                # \U0001f4a1 Skip duplicates at the same recursion level
                #
                # If the current number is the same as the previous one,
                # and we're still at the same level of decision-making
                # (i.e., same recursive call), we skip it to avoid 
                # generating duplicate combinations.
                #
                # Why does `i > index` mean "same recursion level"?
                # Because `index` is where this loop started in this call.
                # If `i > index`, we're just moving through options at this level.
                #
                # So if nums[i] == nums[i-1], and we're not at the start
                # of this level (i > index), then we've already tried
                # this number once at this level and should skip it now.
                #
                # Example: For nums = [1, 1, 2] and target = 3, without this check, both [1, 2] and [1, 2] could be added.
                # With this check, we take only the first 1 at each level, and skip the rest that would lead to the same path.
                # It is safe to take duplicates at *different levels*, just not at the same one.


                # ⚠️ This is key to avoid duplicate combinations.
                # -----------------------------------------------
                if i > index and nums[i] == nums[i - 1]:
                    continue

                # If the current candidate exceeds the target, we can stop early (array is sorted)
                if nums[i] > target_remaining:
                    break

                # Choose the current number
                current_combination.append(nums[i])

                # Recurse with updated target and move to next index (no reuse of same element)
                backtrack(i + 1, target_remaining - nums[i], current_combination, nums, all_combinations)

                # Backtrack: undo the last choice
                current_combination.pop()

        # Sort the input to handle duplicates and allow early stopping
        candidates.sort()
        result = []
        backtrack(0, target, [], candidates, result)
        return result"""
\U0001f501 Recursion Tree Example for candidates = [1, 1, 2], target = 3
(sorted: [1, 1, 2])

                         []
                        /  \
                   [1]       (skip second 1 here at same level)
                   /  \
              [1,1]   [1,2]
               /         \
        [1,1,2] (too big)  [1,2] ✅

Valid combinations:
- [1,2]
- [1,1] (then combined with another 1 would go over target, so we avoid it)
- [1,1,2] is invalid (sum > 3)

✅ Using i > index avoids picking the second 1 at the same level to prevent duplicate [1,2]
"""
