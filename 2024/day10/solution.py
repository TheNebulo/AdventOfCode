with open('./2024/day10/input.txt', 'r') as file:
    map = [line.strip() for line in file.readlines()]

y_max = len(map) - 1
x_max = len(map[0]) - 1

def coordinates_exist(y,x):
    if y > y_max or y < 0: return False
    if x > x_max or x < 0: return False
    return True

def get_visitable_coordinates(pos):
    y, x = pos
    adjacents = [(y+1, x),(y, x+1),(y-1, x),(y, x-1)]
    
    def filter_func(adjacent):
        if not coordinates_exist(*adjacent): return False
        return map[adjacent[0]][adjacent[1]] == str(int(map[y][x]) + 1)
    
    return list(filter(filter_func, adjacents))

def find_peaks(head_pos: tuple[int, int]):
    if map[head_pos[0]][head_pos[1]] == '9': return [head_pos], 1
    
    visitable_coords = get_visitable_coordinates(head_pos)
    if len(visitable_coords) == 0: return [], 0
    
    peaks = []
    routes = 0
    
    for pos in visitable_coords:
        peak_coords, number_of_routes = find_peaks(pos)
        
        routes += number_of_routes
        for peak_pos in peak_coords:
            if peak_pos in peaks: continue
            peaks.append(peak_pos)
    
    return peaks, routes

trailhead_sum = 0
rating_sum = 0
for y in range(y_max + 1):
    for x in range(x_max + 1):
        if map[y][x] == '0': 
            peaks, routes = find_peaks((y,x))
            trailhead_sum += len(peaks)
            rating_sum += routes
        
print("Answer to part 1:", trailhead_sum)
print("Answer to part 2:", rating_sum)