class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index=haystack.find(needle,0,len(haystack))
        
        return index
        if not index:
            return -1
        
            
                            