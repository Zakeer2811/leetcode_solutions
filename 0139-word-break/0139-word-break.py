class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        # Convert wordDict to a set for fast lookups
        word_set = set(wordDict)
        
        # Dictionary to store the results of subproblems
        memo = {}

        # Helper function to check if a substring starting at 'start' can be segmented
        def canSegment(start):
            # If we've already computed the result for this index, return it
            if start in memo:
                return memo[start]

            # If we reach the end of the string, it means the string can be segmented
            if start == len(s):
                return True
            
            # Try all possible end indices for the current word
            for end in range(start + 1, len(s) + 1):
                # Extract the current substring s[start:end]
                if s[start:end] in word_set:
                    # If the substring is a word, check if the remaining string can be segmented
                    if canSegment(end):
                        memo[start] = True  # Store result in memo
                        return True

            # If no valid segmentation is found, store result as False and return
            memo[start] = False
            return False
        
        # Start recursion from index 0
        return canSegment(0)


# Recursion Tree (Text Representation):

# WordDict = ["apple", "pen"]
# String = "applepenapple"

# Can we segment "applepenapple" starting from index 0?

# Recursion starts at index 0 with string "applepenapple":
# 1. First we check "apple" (index 0 to 5), which is in the dictionary.
#    → Recursion proceeds with substring "penapple" starting at index 5.

#     Substring: "penapple"
#     2. Next, we check "pen" (index 5 to 8), which is in the dictionary.
#        → Recursion proceeds with substring "apple" starting at index 8.

#         Substring: "apple"
#         3. Finally, we check "apple" (index 8 to 13), which is in the dictionary.
#            → Reached the end of the string (index 13 == len(s)), returns True.

# Therefore, the valid segmentation path is: ["apple", "pen", "apple"].
# The recursion returns True, indicating that the string can be segmented.

# Example of Recursion Tree:

#                    canSegmentFromIndex(0, "applepenapple")
#                             |
#                       Checks "apple" (index 0 to 5)
#                             |
#                  canSegmentFromIndex(5, "penapple")
#                             |
#                       Checks "pen" (index 5 to 8)
#                             |
#                  canSegmentFromIndex(8, "apple")
#                             |
#                       Checks "apple" (index 8 to 13)
#                             |
#                   Reached end of string (index 13)
#                             |
#                       Returns True
#                             |
#                   Final valid segmentation: ["apple", "pen", "apple"]
# Initial Call:
# canSegmentFromIndex(0, "applepenapple")
#     |
#     Checks: "apple" (index 0 to 5) → proceeds with canSegmentFromIndex(5, "penapple")
#         |
#         Checks: "pen" (index 5 to 8) → proceeds with canSegmentFromIndex(8, "apple")
#             |
#             Checks: "apple" (index 8 to 13) → proceeds with canSegmentFromIndex(13, "")
#                 |
#                 Reached the end of the string, returns True
#                     |
#                 Returns True for all previous calls
#                     |
#                 Final valid segmentation: ["apple", "pen", "apple"]
