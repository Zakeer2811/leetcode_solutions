class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def helper(current, open_count, close_count):
            # Base case: when the current string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Take '(' if we have not used all open brackets yet
            if open_count < n:
                # Take '(' → go deeper with one more open bracket
                helper(current + '(', open_count + 1, close_count)

            # Take ')' if it would not invalidate the string
            if close_count < open_count:
                # Take ')' → go deeper with one more close bracket
                helper(current + ')', open_count, close_count + 1)

        # Start the recursion with an empty string
        helper('', 0, 0)
        return result

        # ------------------------------------------------
        # RECURSION TREE for n = 2 explained as Take / Not Take
        #
        #                      (0, 0, '')
        #                          |
        #         Take '('       (1, 0, '(')
        #                     /             \
        #     Take '('     (2, 0, '((')    Take ')'  (1, 1, '()')
        #                 /                    \
        # Take ')'    (2, 1, '(()')       Take '('  (2, 1, '()(')
        #              /                        \
        # Take ')' (2, 2, '(())')           Take ')' (2, 2, '()()')
        #         |                                 |
        #   res.append('(())')                res.append('()()')
        #
        # Each node represents:
        #   - (open_count, close_count, current_string)
        # At each step:
        #   - "Take '('": if open_count < n
        #   - "Take ')'": if close_count < open_count
        #
        # This way, we only build valid parentheses combinations.
        # ------------------------------------------------
