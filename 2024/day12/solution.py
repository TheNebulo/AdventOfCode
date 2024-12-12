with open('./2024/day12/input.txt', 'r') as file:
    map = [line.strip() for line in file.readlines()]

y_max = len(map) - 1
x_max = len(map[0]) - 1

def coordinates_exist(y,x):
    if y > y_max or y < 0: return False
    if x > x_max or x < 0: return False
    return True

def get_visitable_coordinates(pos, blacklist):
    y, x = pos
    cur_val = map[y][x]
    adjacents = [(y+1, x),(y, x+1),(y-1, x),(y, x-1)]
    
    def filter_func(adjacent):
        if not coordinates_exist(*adjacent): return False
        if adjacent in blacklist: return False
        return map[adjacent[0]][adjacent[1]] == cur_val
    
    return list(filter(filter_func, adjacents))

def find_region(letter, head_pos: tuple[int, int], blacklist):
    if map[head_pos[0]][head_pos[1]] != letter: return blacklist
    blacklist.append(head_pos)
    
    visitable_coords = get_visitable_coordinates(head_pos, blacklist)
    if len(visitable_coords) == 0: return blacklist
    
    for pos in visitable_coords: blacklist = find_region(letter, pos, blacklist)
    
    return blacklist

def is_in_region(y,x, regions):
    for region in regions:
        if (y,x) in region: return True
    return False

def calculate_region_perimeter(region): # This needs to be adjusted for part 2, idk how yet
    region = list(set(region))
    perimeter = 0
    for y, x in region:
        for plot in [(y+1, x),(y, x+1),(y-1, x),(y, x-1)]: 
            if plot not in region: perimeter += 1
    return perimeter

print("This solution takes a moment or two, wait a little :)")

regions = []
price = 0
for y in range(y_max + 1):
    for x in range(x_max + 1):
        if is_in_region(y, x, regions): continue
        regions.append(list(set(find_region(map[y][x], (y,x), []))))
        price += len(regions[-1]) * calculate_region_perimeter(regions[-1])

print("Answer to part 1:", price)  
print("Answer to part 2: NOT READY YET") # cba rn  