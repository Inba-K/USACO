import sys

def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    zyx = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    atbash_table = str.maketrans(abc, zyx)
    
    print(input_data.translate(atbash_table))

if __name__ == '__main__':
    main()
