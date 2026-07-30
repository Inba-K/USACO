import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    Q = int(input_data[0])
    kernels = [True] * 100001
    lit_count = 100000
    
    idx = 1
    
    for _ in range(Q):
        for _ in range(10):
            kernel_id = int(input_data[idx])
            idx += 1
            
            if kernels[kernel_id]:
                kernels[kernel_id] = False
                lit_count -= 1
            else:
                kernels[kernel_id] = True
                lit_count += 1
                
        sys.stdout.write(str(lit_count) + '\n')

if __name__ == '__main__':
    solve()
