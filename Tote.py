from collections import Counter

def solve():
    P = input().strip()
    counts = Counter(P)
    
    digit_counts = [0] * 10
    
    digit_counts[0] = counts['Z']
    digit_counts[2] = counts['W']
    digit_counts[4] = counts['U']
    digit_counts[6] = counts['X']
    digit_counts[8] = counts['G']
    
    digit_counts[3] = counts['H'] - digit_counts[8]
    digit_counts[5] = counts['F'] - digit_counts[4]
    digit_counts[7] = counts['S'] - digit_counts[6]
    digit_counts[1] = counts['O'] - digit_counts[0] - digit_counts[2] - digit_counts[4]
    digit_counts[9] = counts['I'] - digit_counts[5] - digit_counts[6] - digit_counts[8]
    
    all_digits = []
    for digit in range(10):
        all_digits.extend([digit] * digit_counts[digit])
        
    first_digit_idx = next(i for i, d in enumerate(all_digits) if d > 0)
    first_digit = all_digits.pop(first_digit_idx)
    
    ans = [str(first_digit)] + [str(d) for d in all_digits]
    print("".join(ans))

if __name__ == '__main__':
    solve()
