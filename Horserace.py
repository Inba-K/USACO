import sys
from fractions import Fraction
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    
    X = [int(x) for x in input_data[1:N+1]]
    S = [int(s) for s in input_data[N+1:2*N+1]]

    max_horses = 1

    for i in range(N):
        time_counts = defaultdict(int)
        currently_together = 1
        for j in range(N):
            if i == j:
                continue

            delta_X = X[i] - X[j]
            delta_S = S[j] - S[i]

            if delta_S == 0:
                if delta_X == 0:
                    currently_together += 1
                continue

            if (delta_X >= 0 and delta_S > 0) or (delta_X <= 0 and delta_S < 0):
                t = Fraction(abs(delta_X), abs(delta_S))
                time_counts[t] += 1

        max_horses = max(max_horses, currently_together)
        for count in time_counts.values():
            max_horses = max(max_horses, currently_together + count)

    return max_horses

print(solve())
