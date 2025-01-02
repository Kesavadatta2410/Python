def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapsack(W, wt, val, n - 1)
    else:
        # Fixing the second recursive call within max function
        return max(val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1), knapsack(W, wt, val, n - 1))

# Example usage
val = [50, 100, 150, 200]
wt = [8, 16, 32, 40]
W = 64
n = len(val)
print(knapsack(W, wt, val, n))