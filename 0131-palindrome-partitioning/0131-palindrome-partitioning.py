from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # List to store all possible partitions of palindromic substrings
        all_palindrome_partitions = []  
        
        # Temporary list to store the current partition during backtracking
        current_partition = []  
        
        # Helper function to perform backtracking
        def backtrack(start_index: int):
            # Base case: if we have processed the entire string, add the current partition to the result
            if start_index == len(s):
                all_palindrome_partitions.append(current_partition[:])  # Add a copy of current partition
                return
            
            # Try partitioning the string at different points, starting from 'start_index'
            for end_index in range(start_index, len(s)):
                # Extract the substring from start_index to end_index (inclusive)
                substring = s[start_index:end_index + 1]
                
                # Check if the substring is a palindrome
                if is_palindrome(substring):
                    # If it's a palindrome, add it to the current partition
                    current_partition.append(substring)
                    # Recurse with the remaining substring
                    backtrack(end_index + 1)
                    # Backtrack: remove the last added palindrome substring and try another option
                    current_partition.pop()
        
        # Helper function to check if a given substring is a palindrome
        def is_palindrome(substring: str) -> bool:
            # A palindrome reads the same forwards and backwards
            return substring == substring[::-1]
        
        # Start the backtracking from index 0
        backtrack(0)
        
        # Return all the possible palindromic partitions
        return all_palindrome_partitions

#
# Recursion Tree for input "aabb":
# We are trying all possible palindromic substrings and backtracking when needed.

# First recursive call: helper("aabb", [], [])
#    - Try substring "a" -> curr = ['a'], recurse on "abb"
#       - helper("abb", ['a'], [])
#           - Try substring "a" -> curr = ['a', 'a'], recurse on "bb"
#              - helper("bb", ['a', 'a'], [])
#                  - Try substring "b" -> curr = ['a', 'a', 'b'], recurse on "b"
#                     - helper("b", ['a', 'a', 'b'], [])
#                         - Try substring "b" -> curr = ['a', 'a', 'b', 'b'], recurse on ""
#                            - helper("", ['a', 'a', 'b', 'b'], []) -> Valid Partition ['a', 'a', 'b', 'b']
#                     - Backtrack: Remove 'b' -> curr = ['a', 'a', 'b']
#                  - Try substring "bb" -> curr = ['a', 'a', 'bb'], recurse on ""
#                     - helper("", ['a', 'a', 'bb'], []) -> Valid Partition ['a', 'a', 'bb']
#              - Backtrack: Remove 'b' -> curr = ['a', 'a']
#           - Backtrack: Remove 'a' -> curr = ['a']
#       - Try substring "aa" -> curr = ['aa'], recurse on "bb"
#           - helper("bb", ['aa'], [])
#               - Try substring "b" -> curr = ['aa', 'b'], recurse on "b"
#                  - helper("b", ['aa', 'b'], [])
#                      - Try substring "b" -> curr = ['aa', 'b', 'b'], recurse on ""
#                         - helper("", ['aa', 'b', 'b'], []) -> Valid Partition ['aa', 'b', 'b']
#                  - Backtrack: Remove 'b' -> curr = ['aa', 'b']
#               - Try substring "bb" -> curr = ['aa', 'bb'], recurse on ""
#                  - helper("", ['aa', 'bb'], []) -> Valid Partition ['aa', 'bb']
#           - Backtrack: Remove 'bb' -> curr = ['aa']
#       - Backtrack: Remove 'aa' -> curr = []
#    - Backtrack: Remove 'a' -> curr = []
# Final result: [['a', 'a', 'b', 'b'], ['a', 'a', 'bb'], ['aa', 'b', 'b'], ['aa', 'bb']]
'''
helper("aabb", [], []) 
|
|--> helper("abb", ['a'], [])
|    |
|    |--> helper("bb", ['a', 'a'], [])
|    |    |
|    |    |--> helper("b", ['a', 'a', 'b'], [])
|    |    |    |
|    |    |    |--> helper("", ['a', 'a', 'b', 'b'], []) -> valid partition
|    |    |
|    |    |--> helper("", ['a', 'a', 'bb'], []) -> valid partition
|    |
|    |--> helper("aa", ['aa'], [])
|         |
|         |--> helper("b", ['aa', 'b'], [])
|         |    |
|         |    |--> helper("b", ['aa', 'b', 'b'], [])
|         |    |    |
|         |    |    |--> helper("", ['aa', 'b', 'b'], []) -> valid partition
|         |
|         |--> helper("", ['aa', 'bb'], []) -> valid partition
'''