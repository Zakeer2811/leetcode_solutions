class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}  # Keep track of counts of 'a', 'b', 'c' in current window
        res = 0                          # Result: number of valid substrings found
        left = 0                        # Left pointer of sliding window

        # Move right pointer from 0 to end of string
        for right in range(len(s)):
            count[s[right]] += 1
            # Add current character to the window


            # While the window contains at least one 'a', 'b', and 'c':
            # This means the current window is valid
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # Why do we add (len(s) - right) here?
                # Because all substrings starting at 'left' and ending at or after 'right'
                # are valid. For example, if right = 2, s length = 6,
                # substrings: s[left:right+1], s[left:right+2], ..., s[left:6]
                # will all contain at least one 'a', 'b', and 'c'.
                res += len(s) - right

                # Now, we try to move left pointer forward to find new windows
                # starting at later positions that are also valid.
                count[s[left]] -= 1  # Remove the character at left from the window
                left += 1            # Shrink the window from the left

                # Why move left?
                # Because we want to count *all* valid substrings starting from different positions.
                # Once a valid window is found, shrinking left might still keep it valid,
                # and those substrings should be counted as well.

        return res
# from collections import defaultdict

# class Solution:
#     def plzhelp(self, s: str, k: int) -> int:
#         i = 0
#         count = 0
#         mp = defaultdict(int)  # Dictionary to store counts of characters in current window

#         for j in range(len(s)):
#             mp[s[j]] += 1  # Add current character to the window

#             # Shrink window from the left if we have more than k distinct characters
#             while len(mp) > k:
#                 mp[s[i]] -= 1
#                 if mp[s[i]] == 0:
#                     del mp[s[i]]
#                 i += 1

#             # Add the number of substrings ending at j with at most k distinct characters
#             count += (j - i + 1)

#         return count

#     def numberOfSubstrings(self, s: str) -> int:
#         k = 3
#         # Number of substrings with exactly k distinct characters =
#         # number of substrings with at most k distinct chars - number with at most k-1 distinct chars
#         return self.plzhelp(s, k) - self.plzhelp(s, k - 1)
