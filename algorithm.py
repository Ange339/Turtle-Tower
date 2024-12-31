def solution(turtles):
    turtles.sort(key = lambda x: x[0]+x[1])
    n = len(turtles)
    dp = [[(0, 0) for _ in range(n)] for _ in range(n+1)]

    # base case
    best_turtles = [(0,0) for _ in range(n)]
    
    for i in range(2, n+1):
        curr_best = []
        for j in range(n):
            weight, load = turtles[j]
            if i == 1:
                if j == 0 or curr_best[-1][0] > weight:
                    curr_best.append((weight, 1))
                else:
                    curr_best.append(curr_best[-1])
                dp[1] = (weight, 1)
                continue
    
            if j == 0:
                dp[i][j] = dp[i-1][j]
                curr_best.append(dp[i][j])
                continue
            
            prev = best_turtles[j-1]
            if load >= prev[0]:
                new_tower = (prev[0] + weight, prev[1] + 1)
                
                if (new_tower[1] > dp[i-1][j][1]) or (new_tower[1] == dp[i-1][j][1] and new_tower[0] < dp[i-1][j][0]):
                    dp[i][j] = new_tower
                else:
                    dp[i][j] = dp[i-1][j]
            curr_best.append(max((dp[i][j], curr_best[-1]), key = lambda x: x[1]))
        best_turtles = curr_best
    return dp[-1][-1][-1]

