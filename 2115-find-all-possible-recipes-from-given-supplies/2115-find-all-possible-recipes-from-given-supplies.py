from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Create a dictionary to track available ingredients and recipes
        available = {ingredient: True for ingredient in supplies}  # A map of available ingredients
        ans = []
        recipe_status = {recipe: False for recipe in recipes}  # A map to track if a recipe can be made

        # Keep iterating while we can create new recipes
        flag = True
        
        while flag:
            flag = False
            for i in range(len(recipes)):
                # If the recipe is already available, skip it
                if recipe_status[recipes[i]]:
                    continue
                
                # Check if all ingredients for this recipe are available
                can_create = True
                for ingredient in ingredients[i]:
                    if ingredient not in available:
                        can_create = False
                        break
                
                # If all ingredients are available, we can create this recipe
                if can_create:
                    available[recipes[i]] = True  # Mark the recipe as available
                    recipe_status[recipes[i]] = True  # Mark that this recipe can be created
                    ans.append(recipes[i])
                    flag = True
        
        return ans
