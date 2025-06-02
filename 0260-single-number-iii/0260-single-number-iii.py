from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: Compute XOR of all elements.
        # Since duplicates cancel out in XOR, result will be XOR of two unique numbers.
        xor_of_all = 0
        for num in nums:
            xor_of_all ^= num

        # Step 2: Find the rightmost set bit in xor_of_all.
        # This helps us distinguish the two unique numbers since they differ at this bit.
        # (xor_of_all & (xor_of_all - 1)) removes the rightmost set bit.
        # XORing it back gives us just the rightmost set bit.
        xor_without_rightmost = xor_of_all & (xor_of_all - 1)
        distinguishing_bit = xor_without_rightmost ^ xor_of_all

        # Step 3: Use the distinguishing bit to split numbers into two groups.
        # One group has this bit set, the other doesn't.
        # The two unique numbers fall into different groups.
        unique1 = 0
        unique2 = 0
        for num in nums:
            if num & distinguishing_bit:
                unique1 ^= num  # XOR of first group
            else:
                unique2 ^= num  # XOR of second group

        # Step 4: Return the two unique numbers (order doesn't matter)
        return [unique1, unique2]
