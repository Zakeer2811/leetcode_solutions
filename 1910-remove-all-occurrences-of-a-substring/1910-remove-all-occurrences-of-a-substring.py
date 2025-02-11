class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)  # Replace the first occurrence of 'part' with an empty string
        return s
