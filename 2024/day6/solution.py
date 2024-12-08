import copy

with open('./2024/day6/input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]

y_max = len(lines) - 1
x_max = len(lines[0]) - 1

initial_guard_y = 0
initial_guard_x = 0

def coordinates_exist(y,x):
    if y > y_max or y < 0: return False
    if x > x_max or x < 0: return False
    return True

def get_guard_next_pos(y, x, dir):
    if dir == 0: y -= 1
    if dir == 90: x += 1
    if dir == 180: y += 1
    if dir == 270: x -= 1
    return y, x

def simulate_guard(map, guard_y, guard_x):
    map = copy.deepcopy(map)
    
    dir = 0
    visited_locations = 0
    revisit_count = 0
    
    while True: 
        if map[guard_y][guard_x] != 'X':
            visited_locations += 1
            revisit_count = 0
            map[guard_y][guard_x] = 'X'
        else:
            revisit_count += 1
            
        yield guard_y, guard_x
        
        if revisit_count > max(y_max, x_max): 
            yield -1
            return
        
        next_y, next_x = get_guard_next_pos(guard_y, guard_x, dir)
        if not coordinates_exist(next_y, next_x): break
        
        if map[next_y][next_x] == '#': dir = (dir + 90) % 360
        else: 
            guard_y, guard_x = next_y, next_x
    
    yield visited_locations
    

for y in range(y_max + 1):
    initial_guard_x = ''.join(lines[y]).find('^')
    if initial_guard_x != -1:
        initial_guard_y = y
        break
    
print("This solution takes a while to find due to a time complexity of O(n^2) if not more. Grab a coffee while you wait ;)")

times_stuck_in_loop = 0
placed_obstacle_positions = []
for response in simulate_guard(lines, initial_guard_y, initial_guard_x):
    if type(response) != tuple: 
        print("Answer to part 1:", response)
        break

    pos_y, pos_x = response
    
    map = copy.deepcopy(lines)
    if map[pos_y][pos_x] == '#': continue
    if (pos_y, pos_x) in placed_obstacle_positions: continue
    placed_obstacle_positions.append((pos_y, pos_x))
    map[pos_y][pos_x] = '#'
    
    for response in simulate_guard(map, initial_guard_y, initial_guard_x):
        if response == -1: times_stuck_in_loop += 1
    
print("Answer to part 2:", times_stuck_in_loop)