class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"  # First term

        for _ in range(n - 1):
            result = self.describe(result)
        
        return result

    def describe(self, s: str) -> str:
        count = 1
        say = []
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                say.append(str(count))
                say.append(s[i - 1])
                count = 1  # reset count
        
        # Don't forget the last group
        say.append(str(count))
        say.append(s[-1])

        return ''.join(say)
