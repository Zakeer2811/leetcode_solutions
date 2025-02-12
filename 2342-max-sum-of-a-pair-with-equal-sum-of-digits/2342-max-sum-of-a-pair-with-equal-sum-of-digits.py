class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def nsum(n):
            s=0
            while n:
                s+=n%10
                n//=10
            return s
        def update_top_two(m, key, new_value):
            if key not in m:
                m[key] = [new_value]
            else:
                # Retrieve the current top two values for the key (if they exist)
                largest = m[key][0] if len(m[key]) > 0 else float('-inf')
                second_largest = m[key][1] if len(m[key]) > 1 else float('-inf')

                # Update the largest and second largest numbers
                if new_value > largest:
                    second_largest = largest
                    largest = new_value
                elif new_value > second_largest:
                    second_largest = new_value

                # Update the dictionary with the new top two numbers
                m[key] = [largest, second_largest]
        m=defaultdict(list)
        for i in range(len(nums)):
            n = nums[i]
            key = nsum(n)  # The key is determined by the function nsum(n)
            update_top_two(m, key, n)
        ans=-1
        for k,v in m.items():
            if v and len(v)>1:
                ans=max(ans,sum(v))
        return ans if ans>0 else -1

