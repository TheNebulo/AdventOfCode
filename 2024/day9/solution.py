with open('./2024/day9/input.txt', 'r') as file:
    disk_map = file.readline()
    
expanded_disk_map = []
disk_map_without_space = []
is_file_block = True
id = 0

for char in disk_map:
    amount = int(char)
    
    if is_file_block: 
        for i in range(amount): 
            expanded_disk_map.append(id)
            disk_map_without_space.append(id)
        id += 1
    else:
        for i in range(amount): expanded_disk_map.append(None)
    
    is_file_block = not is_file_block
    
pos = 0
checksum = 0
    
while len(disk_map_without_space) > 0:
    if expanded_disk_map[0] != None:
        checksum += (disk_map_without_space[0] * pos)
        disk_map_without_space.pop(0)
    
    else:
        checksum += (disk_map_without_space[-1] * pos)
        disk_map_without_space.pop(-1)
        
    expanded_disk_map.pop(0)
    pos += 1
        
print("Answer to part 1:", checksum)
print("Answer to part 2: NOT READY YET") # I really can't figure this one out rn haha