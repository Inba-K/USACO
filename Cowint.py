import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    T = int(next(iterator))
    for _ in range(T):
        N = int(next(iterator))
        D = int(next(iterator))
        A = []
        for _ in range(N):
            A.append(int(next(iterator)))
        seen = set(A)
        found = False
        for x in A:
            if (x + D) in seen:
                found = True
                break
        if found:
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    solve()