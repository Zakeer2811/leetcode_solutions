class Solution:
    def fairCandySwap(self, A, B):
        sumA = sum(A)
        sumB = sum(B)
        
        setA = set(A)  # Use a set for O(1) look-up
        dif = (sumA - sumB) // 2  # Difference divided by 2
        
        for candyB in B:
            targetA = candyB + dif
            if targetA in setA:  # Check if the targetA exists in setA
                return [targetA, candyB]
        
        return None
