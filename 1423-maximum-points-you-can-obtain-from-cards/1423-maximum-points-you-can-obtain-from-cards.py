class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # Calculate the sum of the first k cards (from the left)
        left_sum = sum(cardPoints[:k])
        max_score = left_sum
        
        # Use sliding window approach
        for i in range(k):
            # Subtract the last left element and add the corresponding right element
            left_sum -= cardPoints[k - i - 1]
            right_sum = cardPoints[n - i - 1]
            left_sum += right_sum
            # Update the maximum score
            max_score = max(max_score, left_sum)
        
        return max_score
