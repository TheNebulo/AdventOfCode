with open('./2024/day8/input.txt', 'r') as file:
    map = [list(line.strip()) for line in file.readlines()]
    
y_max = len(map) - 1
x_max = len(map[0]) - 1
frequencies = {}
antinodes = []

def coordinates_exist(y,x):
    if y > y_max or y < 0: return False
    if x > x_max or x < 0: return False
    return True

for y in range(y_max + 1):
    for x in range(x_max + 1):
        if map[y][x] == '.': continue
        
        if map[y][x] not in frequencies: frequencies[map[y][x]] = []
        frequencies[map[y][x]].append((y,x))

# Part 1
for locations in frequencies.values():
    for location in locations:
        for other_location in locations:
            if location == other_location: continue
            
            diff = (location[0] - other_location[0], location[1] - other_location[1])
            antinode_location = (location[0] + diff[0], location[1] + diff[1])
            
            if antinode_location in antinodes: continue
            elif coordinates_exist(*antinode_location): antinodes.append(antinode_location)    
non_resonant_antinode_count = len(antinodes)

# Part 2 (Inefficient split into passes, but required to properly seperate part 1 and part 2 answers)
for locations in frequencies.values():
    for location in locations:
        if location not in antinodes: antinodes.append(location)
        
        for other_location in locations:
            if location == other_location: continue
            
            diff = (location[0] - other_location[0], location[1] - other_location[1])
            antinode_location = (location[0] + diff[0], location[1] + diff[1])
            
            while True:
                antinode_location = (antinode_location[0] + diff[0], antinode_location[1] + diff[1])
                if antinode_location in antinodes: continue
                if not coordinates_exist(*antinode_location): break
                antinodes.append(antinode_location)
            
print("Answer to part 1:", non_resonant_antinode_count)
print("Answer to part 2:", len(antinodes))