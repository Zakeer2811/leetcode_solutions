from collections import defaultdict
import heapq

class Solution:
    def clearStars(self, input_str: str) -> str:
        length = len(input_str)  # Get the length of the input string
        min_char_heap = []  # Min-heap to keep track of the smallest characters seen so far
        char_indices_map = defaultdict(list)  # Dictionary to store indices of each character
        keep_char = [True] * length  # A list that will mark whether to keep each character

        # Iterate through the string character by character
        for index, char in enumerate(input_str):
            if char == '*':
                # If we encounter a star ('*'), we need to remove the smallest character to its left
                
                # Get the smallest character from the heap (min-heap ensures this is the smallest one)
                smallest_char = min_char_heap[0]
                heapq.heappop(min_char_heap)  # Remove the smallest character from the heap
                
                # Find the last occurrence index of the smallest character using our dictionary
                last_occurrence_idx = char_indices_map[smallest_char].pop()
                
                # Mark the current '*' and the smallest character's position as removed
                keep_char[index] = False  # Remove the '*' from the result
                keep_char[last_occurrence_idx] = False  # Remove the smallest character from the result
                
            else:
                # If it's a regular character, push it onto the min-heap
                # This will allow us to track the lexicographically smallest characters to the left
                heapq.heappush(min_char_heap, char)
                
                # Keep track of where each character appears in the string by storing their indices
                char_indices_map[char].append(index)

        # Now, we want to build the final result string by including only characters that are not marked for removal
        result_chars = [input_str[i] for i in range(length) if keep_char[i]]
        
        # Return the result string by joining the characters that we kept
        return "".join(result_chars)
