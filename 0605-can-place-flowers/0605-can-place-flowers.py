class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Check next and prev flower bed values. If i is at the ends, assume next and prev as 0.
                next_flower = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
                prev_flower = flowerbed[i - 1] if i > 0 else 0
                if next_flower == 0 and prev_flower == 0:
                    flowerbed[i] = 1
                    count += 1
            if count >= n:  # Stop if we've already placed enough flowers
                break
        return count >= n
