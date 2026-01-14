class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        def divisors(l):
            return [d for d in range(1, l) if l % d == 0]
        
        def cost(i, j):
            l = j - i + 1
            if l < 2:
                return 10**9
            ds = divisors(l)
            if not ds:
                return 10**9
            ans = 10**9
            for d in ds:
                c = 0
                for st in range(d):
                    ch = [s[i + st + d*x] for x in range(l//d)]
                    lt, rt = 0, len(ch)-1
                    while lt < rt:
                        if ch[lt] != ch[rt]:
                            c += 1
                        lt += 1
                        rt -= 1
                ans = min(ans, c)
            return ans
        
        ct = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                ct[i][j] = cost(i, j)
        
        INF = 10**9
        dp = [[INF]*(k+1) for _ in range(n+1)]
        dp[0][0] = 0
        
        for i in range(2, n+1):
            for j in range(1, min(i//2, k)+1):
                for p in range(2*(j-1), i-1):
                    if dp[p][j-1] < INF:
                        dp[i][j] = min(dp[i][j], dp[p][j-1] + ct[p][i-1])
        
        return dp[n][k]