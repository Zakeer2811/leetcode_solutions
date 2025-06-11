import math

class BITMin:
    """Fenwick‐tree (1‑indexed) supporting point‐updates of min
       and prefix‐min queries over [0..idx]."""
    def __init__(self, size):
        self.N = size
        self.tree = [math.inf] * (size + 1)

    def update(self, idx, val):
        # set tree[idx] = min(tree[idx], val)
        i = idx + 1
        while i <= self.N:
            if val < self.tree[i]:
                self.tree[i] = val
            i += i & -i

    def prefix_min(self, idx):
        # returns min(tree[0..idx])
        if idx < 0:
            return math.inf
        res = math.inf
        i = idx + 1
        while i > 0:
            if self.tree[i] < res:
                res = self.tree[i]
            i -= i & -i
        return res

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        s_int = [ord(c) - ord('0') for c in s]
        ans = -math.inf

        # Try every ordered pair (a,b), a != b
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                # Prefix arrays of length n+1
                S  = [0] * (n+1)  # net (+1 for a) + (-1 for b)
                pa = [0] * (n+1)  # parity of count(a)
                pb = [0] * (n+1)  # parity of count(b)
                cb = [0] * (n+1)  # absolute count of b

                for i in range(1, n+1):
                    x = s_int[i-1]
                    S[i]  = S[i-1] + (1 if x==a else -1 if x==b else 0)
                    pa[i] = pa[i-1] ^ (1 if x==a else 0)
                    pb[i] = pb[i-1] ^ (1 if x==b else 0)
                    cb[i] = cb[i-1] + (1 if x==b else 0)

                max_cb = cb[-1]
                # One BIT for each parity‐state (pa,pb) ∈ {0,1}×{0,1}
                bits = [BITMin(max_cb+1) for _ in range(4)]

                # Slide window end j from k..n
                for j in range(k, n+1):
                    i = j - k
                    # “Open” prefix i as a potential start of any future window ≥k
                    p_i = pa[i]*2 + pb[i]
                    bits[p_i].update(cb[i], S[i])

                    # We want substring (i,j] with
                    #   pa[j]^pa[i] = 1 (a odd)  ⇒  pa[i] = pa[j]^1
                    #   pb[j]^pb[i] = 0 (b even) ⇒  pb[i] = pb[j]
                    p_query = (pa[j]^1)*2 + pb[j]
                    # And we require cb[j] - cb[i] > 0 ⇒  cb[i] ≤ cb[j] - 1
                    limit = cb[j] - 1
                    best_Si = bits[p_query].prefix_min(limit)
                    if best_Si < math.inf:
                        ans = max(ans, S[j] - best_Si)

        return ans if ans > -math.inf else -1
