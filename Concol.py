import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    subcases = input_data[1:T+1]
    
    for S in subcases:
        length = len(S)
        
        if length % 2 != 0:
            k = (length - 1) // 2
            if S == 'Z' * k + 'A' * (k + 1):
                print("YES")
            else:
                print("NO")
                
        else:
            n = length // 2
            col1 = S[:n]
            col2 = S[n:]
            
            k = 0
            while k < n and col1[n - 1 - k] == 'Z':
                k += 1
                
            if k == n:
                print("NO")
                continue
                
            if k > 0 and col2[n - k:] != 'A' * k:
                print("NO")
                continue
                
            c1 = col1[n - 1 - k]
            c2 = col2[n - 1 - k]
            if ord(c2) != ord(c1) + 1:
                print("NO")
                continue
                
            if col1[:n - 1 - k] != col2[:n - 1 - k]:
                print("NO")
                continue
                
            print("YES")

if __name__ == '__main__':
    solve()
