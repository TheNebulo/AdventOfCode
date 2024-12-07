with open('./2024/day6/input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]

y_max = len(lines) - 1
x_max = len(lines[0]) - 1

def coordinates_exist(y,x):
    if y > y_max or y < 0: return False
    if x > x_max or x < 0: return False
    return True

guard_y = 0
guard_x = 0
guard_dir = 0

def get_next_pos():
    next_y = guard_y
    next_x = guard_x
    
    if guard_dir == 0: next_y -= 1
    if guard_dir == 90: next_x += 1
    if guard_dir == 180: next_y += 1
    if guard_dir == 270: next_x -= 1
    
    return next_y, next_x

for y in range(y_max + 1):
    guard_x = ''.join(lines[y]).find('^')
    if guard_x != -1:
        guard_y = y
        break
    
while True:
    lines[guard_y][guard_x] = 'X'
    
    next_y, next_x = get_next_pos()
    if not coordinates_exist(next_y, next_x): break
    
    if lines[next_y][next_x] == '#':
        guard_dir = (guard_dir + 90) % 360
    else:
        guard_y, guard_x = next_y, next_x
    
visited_locations = 0
for line in lines: visited_locations += line.count('X')
    
print("Answer to part 1:", visited_locations)
print("Answer to part 2: NOT READY YET")