class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            ele=asteroids[i]
            if ele>=0:
                stack.append(ele)
            else:
                while stack and stack[-1]>0 and abs(ele)>stack[-1]:
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(ele)
                elif stack and stack[-1]>0 and abs(ele)==stack[-1]:
                    stack.pop()
                   
        return stack
                
