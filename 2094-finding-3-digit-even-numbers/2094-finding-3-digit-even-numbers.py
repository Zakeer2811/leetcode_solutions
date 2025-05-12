class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
          # Step 1: Collect even digits
        even_digits = {'0', '2', '4', '6', '8'}
        
        # Step 2: Create a set to store valid numbers
        valid_numbers = set()
        
        # Step 3: Generate all permutations of 3 digits from the input
        for perm in itertools.permutations(digits, 3):
            num_str = ''.join(map(str, perm))  # Convert tuple to string
            
            # Step 4: Check for leading zero and even last digit
            if num_str[0] != '0' and num_str[-1] in even_digits:
                valid_numbers.add(int(num_str))  # Add valid number to set
        
        # Step 5: Return sorted list of unique valid numbers
        return sorted(valid_numbers)