class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result_stack = []  # Stack to keep track of surviving asteroids after collisions

        for index in range(len(asteroids)):
            current_asteroid = asteroids[index]

            # If the asteroid is moving right (positive), it can't collide yet — just add to stack
            if current_asteroid >= 0:
                result_stack.append(current_asteroid)

            else:
                # The asteroid is moving left (negative), check for collisions with right-moving ones
                while result_stack and result_stack[-1] > 0 and abs(current_asteroid) > result_stack[-1]:
                    # Right-moving asteroid is smaller — it explodes (remove it)
                    result_stack.pop()

                # After above loop:
                # If stack is empty or top is also moving left — no collision, add current
                if not result_stack or result_stack[-1] < 0:
                    result_stack.append(current_asteroid)

                # If equal size collision: both asteroids explode
                elif result_stack and result_stack[-1] > 0 and abs(current_asteroid) == result_stack[-1]:
                    result_stack.pop()  # Remove the right-moving asteroid, current also destroyed so we will not add it 

                # Else case (e.g., top of stack is bigger) is ignored — left-moving asteroid is destroyed

        return result_stack  # Return final list of asteroids after all collisions
