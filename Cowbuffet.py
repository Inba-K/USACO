import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = [int(x) for x in input_data[1:N+1]]
    F.sort()
    
    dp = [0] * (N + 1)
    
    j = 0 
    
    for i in range(1, N + 1):
        while j < i - 1 and F[i - 1] - F[j] >= 10:
            j += 1
            
        opt1 = dp[i - 1]
        
        opt2 = F[i - 1] + dp[j]
        
        dp[i] = max(opt1, opt2)
        
    print(dp[N])

if __name__ == '__main__':
    solve()