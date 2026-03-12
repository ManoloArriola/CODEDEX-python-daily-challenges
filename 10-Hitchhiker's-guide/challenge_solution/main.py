def minimum_components(components):
    target = 42
    dp = [float("inf")] * (target + 1)
    dp[0] = 0

    for component in components:
        for s in range(target, component - 1, -1):
            if dp[s - component] != float("inf"):
                dp[s] = min(dp[s], dp[s - component] + 1)

    return dp[target] if dp[target] != float("inf") else -1
