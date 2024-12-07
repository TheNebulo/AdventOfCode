with open('./2024/day4/input.txt', 'r') as file:
    lines = file.readlines()
    
y_max = len(lines) - 1
x_max = len(lines[0].strip()) - 1
xmas_found = 0
xmas_crosses_found = 0

def coordinates_exist(y,x):
    if y > y_max or y < 0: return False
    if x > x_max or x < 0: return False
    return True

def part_1(y,x):
    global xmas_found
    if lines[y][x] != 'X': return
        
    adjacents = [(y+1, x),(y+1, x+1),(y, x+1),(y-1, x+1),(y-1, x),(y-1, x-1),(y, x-1),(y+1, x-1)]
        
    for (y2, x2) in adjacents:
        if not coordinates_exist(y2, x2): continue
        if lines[y2][x2] != 'M': continue
            
        y3 = y + (2 * (y2 - y))
        y4 = y + (3 * (y2 - y))
        x3 = x + (2 * (x2 - x))
        x4 = x + (3 * (x2 - x))
            
        if not coordinates_exist(y3, x3) or not coordinates_exist(y4, x4): continue
            
        if lines[y3][x3] != 'A': continue
        if lines[y4][x4] != 'S': continue
        xmas_found += 1
        
def part_2(y,x):
    # I hate this solution but 3am coding got the better of me
    global xmas_crosses_found
    if lines[y][x] != 'A': return
    
    if not coordinates_exist(y+1, x+1): return
    if not coordinates_exist(y+1, x-1): return
    if not coordinates_exist(y-1, x+1): return
    if not coordinates_exist(y-1, x-1): return
        
    top_left = lines[y+1][x-1]
    top_right = lines[y+1][x+1]
    bottom_left = lines[y-1][x-1]
    bottom_right = lines[y-1][x+1]
    
    if 'X' in [top_left, top_right, bottom_left, bottom_right]: return
    if 'A' in [top_left, top_right, bottom_left, bottom_right]: return
    if top_left == 'M' and bottom_right != 'S': return
    if top_left == 'S' and bottom_right != 'M' : return
    if top_right == 'M' and bottom_left != 'S': return
    if top_right == 'S' and bottom_left != 'M' : return
    
    xmas_crosses_found += 1
    

for y in range(y_max + 1):
    for x in range(x_max + 1):
        part_1(y,x)
        part_2(y,x)
            
print("Answer to part 1:", xmas_found)
print("Answer to part 2:", xmas_crosses_found)