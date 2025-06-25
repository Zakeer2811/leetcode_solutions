from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        # ⚙️ Helper function to simulate ceiling division
        # We use this when a is negative to compute the smallest integer >= x / a
        def div_ceil(x, y):
            # If x and y have the same sign, integer division behaves like floor and is correct
            # If they have opposite signs, Python's // rounds down, so we compensate to round up
            return math.ceil(x / y)

        # \U0001f50d Counts how many pairs (i, j) exist such that nums1[i] * nums2[j] <= x
        def count_less_equal(x):
            count = 0
            for a in nums1:
                # \U0001f4cc CASE 1: a == 0
                if a == 0:
                    # Product is always 0 regardless of nums2[j]
                    # If x >= 0, then 0 <= x → all products are valid
                    if x >= 0:
                        count += len(nums2)
                    # If x < 0, then 0 > x → none of the zero products are valid
                    # So we add nothing to count

                # \U0001f4cc CASE 2: a > 0
                elif a > 0:
                    # When a is positive, the product increases with nums2[j]
                    # So we need the number of nums2[j] such that:
                    #    a * nums2[j] <= x  ⇒ nums2[j] <= x // a
                    # Since nums2 is sorted, we use bisect_right to find how many
                    # elements are <= x // a
                    pos_limit = x // a
                    count += bisect_right(nums2, pos_limit)

                # \U0001f4cc CASE 3: a < 0
                else:
                    # When a is negative, the product *decreases* with nums2[j]
                    # So we want:
                    #    a * nums2[j] <= x  ⇒ nums2[j] >= ceil(x / a)
                    # That is, we want all nums2[j] ≥ ceil(x / a)
                    # Since nums2 is sorted, we use bisect_left to find the first index
                    # where nums2[j] ≥ ceil(x / a), and subtract from len(nums2)
                    # to get count of such values
                    ceil_div = div_ceil(x, a)
                    idx = bisect_left(nums2, ceil_div)
                    count += len(nums2) - idx
            return count

        # \U0001f9e0 Binary search over all possible product values
        # Why this range? Because nums1[i], nums2[j] ∈ [-1e5, 1e5]
        # So their product can be as low as -1e10 and as high as 1e10
        left= min(nums1[0]*nums2[0], nums1[-1]*nums2[-1], nums1[0]*nums2[-1], nums1[-1]*nums2[0])
        right = max(nums1[0]*nums2[0], nums1[-1]*nums2[-1], nums1[0]*nums2[-1], nums1[-1]*nums2[0])


        # \U0001f9ed Binary search to find the smallest product value such that
        # at least 'k' products are ≤ that value
        while left < right:
            mid = (left + right) // 2  # Try this product value

            # Check how many products are ≤ mid
            count = count_less_equal(mid)

            if count < k:
                # Too few products ≤ mid, so mid is too small
                # Need to move to a higher product value
                left = mid + 1
            else:
                # Enough products ≤ mid, might be the answer
                # Try to find a smaller valid value (move left)
                right = mid

        # \U0001f4cc When loop ends, 'left' is the smallest product
        # such that at least 'k' products are ≤ it
        return left
