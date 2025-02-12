from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def nsum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s
        
        # Dictionary to store the largest and second largest for each key
        m = defaultdict(lambda: [float('-inf'), float('-inf')])
        
        # Initialize the maximum sum variable
        max_sum = -1
        
        # Iterate through nums and update the dictionary
        for num in nums:
            key = nsum(num)  # The key is determined by the function nsum(n)
            
            # Retrieve the current top two values for the key
            largest, second_largest = m[key]
            
            # Update the largest and second largest numbers
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num
            
            # Update the dictionary with the new top two numbers
            m[key] = [largest, second_largest]
            
            # Update the maximum sum if there are two numbers for this key
            if second_largest != float('-inf'):
                max_sum = max(max_sum, largest + second_largest)
        
        return max_sum if max_sum != -1 else -1
