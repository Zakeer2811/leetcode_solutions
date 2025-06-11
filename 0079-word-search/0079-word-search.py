class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(r, c, res, word, board):
            # Base case: If we've matched the word, return True
            if res == word:
                return True
            
            # Boundary check
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == '#':
                return False  # return False if out of bounds or already visited

            # Current character should match the word
            if board[r][c] != word[len(res)]:
                return False
            
            # Mark the current cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all four directions (up, down, left, right)
            if helper(r+1, c, res+temp, word, board):
                return True
            if helper(r-1, c, res+temp, word, board):
                return True
            if helper(r, c+1, res+temp, word, board):
                return True
            if helper(r, c-1, res+temp, word, board):
                return True
            
            # Backtrack: unmark the current cell
            board[r][c] = temp
            
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if helper(r, c, '', word, board):
                    return True
        return False
