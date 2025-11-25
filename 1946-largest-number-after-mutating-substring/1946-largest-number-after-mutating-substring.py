class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        l = list(num)
        mutated = False

        for i in range(len(num)):
            original = int(num[i])
            mapped = change[original]

            # If mapped digit is larger → start mutating
            if mapped > original:
                l[i] = str(mapped)
                mutated = True

            # If mapped digit is smaller after we started → stop mutation
            elif mapped < original and mutated:
                break

            # else (mapped == original) → do nothing

        return "".join(l)
