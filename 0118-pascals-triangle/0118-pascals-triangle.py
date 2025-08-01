class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the DP table to store the Pascal's triangle rows
        dp = []
        
        # Loop through each row from 0 to numRows-1
        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)
            
            # Fill in the values between the first and last element of the row
            for j in range(1, i):
                row[j] = dp[i-1][j-1] + dp[i-1][j]
            
            # Append the row to the DP table
            dp.append(row)
        
        return dp
