from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)  # Frequency map for nums2

    def add(self, index, val):
        old_value = self.nums2[index]
        self.nums2[index] += val  # Update nums2 at the given index
        new_value = self.nums2[index]
        
        # Update frequency map
        self.freq2[old_value] -= 1
        if self.freq2[old_value] == 0:
            del self.freq2[old_value]
        
        self.freq2[new_value] += 1

    def count(self, tot):
        count_pairs = 0
        # For each number in nums1, find how many elements in nums2 complement it to make the sum `tot`
        for num1 in self.nums1:
            complement = tot - num1
            count_pairs += self.freq2.get(complement, 0)
        return count_pairs
