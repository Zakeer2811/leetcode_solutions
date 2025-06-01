class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        right = 0
        left = 0
        max_length = 0
        charset = set()
        
        while right < length:
            if s[right] not in charset:
                charset.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                charset.remove(s[left])
                left += 1
                
        return max_length
