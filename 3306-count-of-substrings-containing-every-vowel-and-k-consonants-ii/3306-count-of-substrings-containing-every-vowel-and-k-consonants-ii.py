class Solution:
    def isVowel(self, ch: str) -> bool:
        return ch in 'aeiou'

    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        result = 0
        left = 0
        consonantCount = 0
        vowelCount = 0
        vowels = set()

        for right in range(n):
            # Expand window by adding the current character
            if self.isVowel(word[right]):
                vowels.add(word[right])
                vowelCount += 1
            else:
                consonantCount += 1

            # Shrink the window if the consonant count exceeds k
            while consonantCount > k:
                if self.isVowel(word[left]):
                    vowels.discard(word[left])
                    vowelCount -= 1
                else:
                    consonantCount -= 1
                left += 1

            # If the window contains exactly 5 vowels and the consonant count is k, count the valid substrings
            if len(vowels) == 5 and consonantCount == k:
                # Add all valid substrings ending at 'right' (starting from any position between left and right)
                result += (right - left + 1)

        return result
