class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        prev=" "
        ans=[]
        for f in folder:
            s=f[:len(prev)]
            if s!=prev or len(f)==len(prev) or f[len(prev)]!='/':
                ans.append(f)
                prev=f
        return ans
        