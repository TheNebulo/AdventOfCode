from collections import Counter

with open('./2024/day11/input.txt', 'r') as file:
    line = file.readline()
    
stones = [int(char) for char in line.split(' ')]

def blink(n, stones):
    split_cache = {}
    multiplication_cache = {}
    stones_counter = Counter(stones)
    
    for _ in range(1, n+1):
        new_stones_counter = Counter()
        
        for stone, count in stones_counter.items():
            if stone == 0: 
                new_stones_counter[1] += count
            
            elif stone in split_cache:
                new_stones_counter[split_cache[stone][0]] += count
                new_stones_counter[split_cache[stone][1]] += count
                
            elif stone in multiplication_cache: 
                new_stones_counter[multiplication_cache[stone]] += count
            
            elif len(str(stone)) % 2 == 0:
                half_len = len(str(stone))//2
                first_half = int(str(stone)[:half_len])
                second_half = int(str(stone)[half_len:])
                
                split_cache[stone] = [first_half, second_half]
                new_stones_counter[first_half] += count
                new_stones_counter[second_half] += count
            
            else:
                new_stone = stone * 2024
                multiplication_cache[stone] = new_stone
                new_stones_counter[new_stone] += count
                
        stones_counter = new_stones_counter
        
    return sum([i for i in stones_counter.values()])        

print("Answer to part 1:", blink(25, stones))
print("Answer to part 2:", blink(75, stones))