class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Step 1: Remove dashes and convert to uppercase
        s = s.replace("-", "").upper()
        res = []
        count = 0

        # Step 2: Build the result backwards, adding dash after every k characters
        for char in reversed(s):
            res.append(char)
            count += 1
            if count == k:
                res.append('-')
                count = 0

        # Step 3: Remove trailing dash if it exists
        if res and res[-1] == '-':
            res.pop()

        # Step 4: Reverse to get the final string
        return "".join(reversed(res))


"""
EDGE CASES (numbers):

1. Length multiple of k:
   s = "1234-5678", k = 4
   Step 1: "12345678"
   Step 2 (backward grouping):
       add '8','7','6','5' → res = ['8','7','6','5','-']
       add '4','3','2','1' → res = ['8','7','6','5','-','4','3','2','1','-']
   Step 3: pop trailing dash → res = ['8','7','6','5','-','4','3','2','1']
   Reverse → "1234-5678"

2. Length less than k:
   s = "12", k = 3
   Step 1: "12"
   Step 2: add '2','1' → res = ['2','1']  (no dash because count < k)
   Reverse → "12"

3. Length exactly k:
   s = "1-2-3", k = 3
   Step 1: "123"
   Step 2: add '3','2','1' → count = 3 → append dash → res = ['3','2','1','-']
   Step 3: pop trailing dash → res = ['3','2','1']
   Reverse → "123"

4. Length not multiple of k (remainder group at start):
   s = "123-45-6789-0", k = 4
   Step 1: "1234567890" (length 10)
   Step 2 (backward grouping in 4s):
       add '0','9','8','7' → res = ['0','9','8','7','-']
       add '6','5','4','3' → res = ['0','9','8','7','-','6','5','4','3','-']
       add '2','1' → res = ['0','9','8','7','-','6','5','4','3','-','2','1']
   Reverse → "12-3456-7890"

5. All dashes and mixed single digits:
   s = "--1-2-3-4--", k = 2
   Step 1: "1234"
   Step 2 (backward in 2s):
       add '4','3' → res = ['4','3','-']
       add '2','1' → res = ['4','3','-','2','1','-']
   Step 3: pop trailing dash → res = ['4','3','-','2','1']
   Reverse → "12-34"
"""

# class Solution:
#     def licenseKeyFormatting(self, s: str, k: int) -> str:
#         s1=""
#         for i in s:
#             if i!='-':
#                 s1+=i.upper()
#         n1=len(s1)
#         res=""
#         if n1%k==0:
#             j=0
#             for i in range(int(n1/k)):
#                 res+=s1[j:j+k]+"-"
#                 j+=k
#         else:
#             first=n1%k
#             res=s1[:first]+"-"
#             j=first
#             for i in range(int(n1/k)):
#                 res+=s1[j:j+k]+"-"
#                 j+=k
#         return res[:-1]

            