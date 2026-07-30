import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    Q = int(input_data[1])
    
    diff = [0] * (N + 2)
    
    idx = 2
    for _ in range(Q):
        S = int(input_data[idx])
        A = int(input_data[idx+1])
        B = int(input_data[idx+2])
        idx += 3
        
        diff[A] += S
        diff[B + 1] -= S
        
    current_seeds = 0
    result = []
    for i in range(1, N + 1):
        current_seeds += diff[i]
        result.append(str(current_seeds))
        
    print(" ".join(result))

if __name__ == '__main__':
    solve()
