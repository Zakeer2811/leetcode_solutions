class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix = 0
        first_occ = {}
        ans = 0

        for i, h in enumerate(hours):
            prefix += 1 if h > 8 else -1

            # Case 1: whole interval from start is well performing
            if prefix > 0:
                ans = max(ans, i + 1)

            # Case 2: need to find prefix - 1
            else:
                if (prefix - 1) in first_occ:
                    ans = max(ans, i - first_occ[prefix - 1])

            # Store first occurrence of this prefix sum
            if prefix not in first_occ:
                first_occ[prefix] = i

        return ans
