class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[]
        for s in spells:
            cnt=0
            for p in potions:
                if s*p>=success:
                    cnt+=1
            ans.append(cnt)
        return ans

        