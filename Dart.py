import sys
from collections import Counter

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    S = int(data[0])
    labels = [int(x) for x in data[1:]]
    
    counts = Counter(labels)
    
    unique_labels = sorted(counts.keys())
    
    ans = []
    
    for x in unique_labels:
        while counts[x] > 0:
            ans.append(x)
            counts[x] -= 1
            counts[2 * x] -= 1
            counts[3 * x] -= 1
            
    print(*(sorted(ans)))

if __name__ == '__main__':
    solve()
