import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    first_line = input_data[0].split()
    N = int(first_line[0])
    M = int(first_line[1])
    K = int(first_line[2])

    last_seen = {}

    for i in range(1, N + 1):
        themes = input_data[i].split()
        
        disliked = False
        for theme in themes:
            if theme in last_seen:
                if i - last_seen[theme] <= K:
                    disliked = True
            
        if disliked:
            print("BOO")
        else:
            print("MOO")
            
        for theme in themes:
            last_seen[theme] = i

if __name__ == '__main__':
    solve()