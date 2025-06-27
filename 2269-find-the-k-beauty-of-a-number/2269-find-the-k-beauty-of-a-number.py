class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        snum = str(num)
        for i in range(len(snum) - k + 1):
            s = snum[i:i + k]
            n = int(s)
            if n == 0:
                continue
            if num % n == 0:
                ans += 1
        return ans
