class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
       
        maxele = max(candies)
        start = 0
        end = maxele
        ans = 0

        while start <= end:
            mid = start + (end - start) // 2

            if self.fun(candies, mid, k):
                if mid > ans:
                    ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans

    def fun(self, arr, mid, k):
        if mid == 0:
            return True

        count = 0
        for i in range(len(arr)):
            temp = arr[i] // mid
            count += temp

        if count >= k:
            return True

        return False