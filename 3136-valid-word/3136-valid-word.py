class Solution:
    def isValid(self, word: str) -> bool:
        v=c=False
        dl=True
        vowels="AEIOUaeiou"
        cv=Counter(vowels)
        if len(word)<3:
            return False
        for ch in word:
            if not ch.isalnum():
                return False
            elif ch in cv:
                v=True
            elif ch not in cv:
                c=True
        res=c and v
        return res&dl
            

        