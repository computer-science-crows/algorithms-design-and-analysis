import numpy as np

def dynamic_solution(n,m,a,s):

    p = max(m,n)

    dp = np.full((1<<(p+1),p),np.inf)
    cost = np.zeros((p+1,p))
    cost[:n,:m]=s

    for i in range(p):
        dp[1<<i][i] = 0

    for mask in range(1<<p):
        print(mask)
        print(dp)
        for i in range(p):
            print(dp[mask][i])
            if dp[mask][i] is float('inf'):
                continue
            for j in range(p):
                if mask and (1<<j) != 0:
                    continue
                dp[mask | (1<<j)][j]=min(dp[mask | (1<<j)][j],dp[mask][i]+cost[i][j])
    
    return dp[n][m]

