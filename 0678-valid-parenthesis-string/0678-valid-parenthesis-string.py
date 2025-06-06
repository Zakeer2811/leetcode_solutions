class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # Minimum possible number of open parentheses
        cmax = 0  # Maximum possible number of open parentheses

        for c in s:
            if c == '(':
                cmin += 1
                cmax += 1
            elif c == ')':
                cmin -= 1
                cmax -= 1
            elif c == '*':
                cmin -= 1   # If '*' is considered as ')'
                cmax += 1   # If '*' is considered as '('

            if cmax < 0:
                return False  # Too many ')' unmatched

            cmin = max(cmin, 0)  # cmin cannot go below 0

        return cmin == 0  # All open parentheses are matched
