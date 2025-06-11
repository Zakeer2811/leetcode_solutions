from typing import List
class Solution:
    def addOperators(self,num: str, target: int) -> List[str]:
        result = []

        def backtrack(index: int, path: str, value: int, prev: int):
            """
            index: current position in the num string
            path: the expression built so far
            value: the current evaluated result of the expression
            prev: the last operand in the expression (used for correct multiplication)
            """
            # Base case: if we've used all digits
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            # Try every possible split from current index to end
            for i in range(index + 1, len(num) + 1):
                curr_str = num[index:i]  # Current substring of num
                if len(curr_str) > 1 and curr_str[0] == '0':
                    break  # Skip numbers with leading zeros

                curr = int(curr_str)

                if index == 0:
                    # First number, just take it without any operator
                    backtrack(i, curr_str, curr, curr)
                else:
                    # ADDITION: Add '+' and update value and prev
                    backtrack(i, path + '+' + curr_str, value + curr, curr)
                    # SUBTRACTION: Add '-' and update value and prev
                    backtrack(i, path + '-' + curr_str, value - curr, -curr)
                    # MULTIPLICATION: Handle precedence
                    # value - prev + (prev * curr) is the key to maintaining proper precedence
                    backtrack(i, path + '*' + curr_str, value - prev + (prev * curr), prev * curr)

        backtrack(0, "", 0, 0)
        return result
'''
num="123" target=6
Start with "" (index = 0)

1
├── +2
│   ├── +3      → 1 + 2 + 3 = 6 ✅
│   ├── -3      → 1 + 2 - 3 = 0
│   └── *3      → 1 + 2*3 = 7
├── -2
│   ├── +3      → 1 - 2 + 3 = 2
│   ├── -3      → 1 - 2 - 3 = -4
│   └── *3      → 1 - 2*3 = -5
└── *2
    ├── +3      → 1*2 + 3 = 5
    ├── -3      → 1*2 - 3 = -1
    └── *3      → 1*2*3 = 6 ✅

Valid expressions:
- "1+2+3"
- "1*2*3"


num="232" target=8
2
├── +3
│   ├── +2  → 2 + 3 + 2 = 7 ❌
│   ├── -2  → 2 + 3 - 2 = 3 ❌
│   └── *2  → 2 + 3 * 2 = 2 + 6 = 8 ✅
├── -3
│   ├── +2  → 2 - 3 + 2 = 1 ❌
│   ├── -2  → 2 - 3 - 2 = -3 ❌
│   └── *2  → 2 - 3 * 2 = 2 - 6 = -4 ❌
└── *3
    ├── +2  → 2 * 3 + 2 = 6 + 2 = 8 ✅
    ├── -2  → 6 - 2 = 4 ❌
    └── *2  → 6 * 2 = 12 ❌

23
├── +2 → 23 + 2 = 25 ❌
├── -2 → 23 - 2 = 21 ❌
└── *2 → 23 * 2 = 46 ❌

232 → value = 232 ❌
'''