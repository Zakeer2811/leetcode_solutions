class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def backtrack(comb,next_digits):
            if len(next_digits)==0:
                return res.append(comb)
            else:
                for letter in phone_map[next_digits[0]]:
                    backtrack(comb+letter,next_digits[1:])
        res=[]
        backtrack('',digits)
        return res
        
            
        