class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        s = set()
        total = 0
        ans = 0  # return 0 if no valid subarray

        for r in range(len(nums)):
            while nums[r] in s:
                s.remove(nums[l])
                total -= nums[l]
                l += 1

            s.add(nums[r])
            total += nums[r]

            if r - l + 1 == k:
                ans = max(ans, total)
                # shrink window from left
                s.remove(nums[l])
                total -= nums[l]
                l += 1

        return ans
