import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    cow_string = input_data[1]
    
    initial_state = [0 if char == 'L' else 1 for char in cow_string]
    
    def get_cost(target_val):
        current = list(initial_state)
        operations = [0] * (N + 1)
        
        flip_count = [0] * (N + 1)
        
        total_energy = 0
        
        for i in range(N, 0, -1):
            
            flips = 0
            for k in range(i, N + 1, i):
                flips += operations[k]
                
            actual_state = (current[i - 1] + flips) % 2
            
            if actual_state != target_val:
                operations[i] = 1
                total_energy += i
                
        return total_energy

    cost_to_L = get_cost(0)
    cost_to_R = get_cost(1)
    
    print(min(cost_to_L, cost_to_R))

if __name__ == '__main__':
    solve()
