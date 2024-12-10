with open('./2024/day9/input.txt', 'r') as file:
    compressed_disk_map = file.readline()
    
print("These answers take a moment to compute due to the sheer size of the input. Please wait a couple seconds.")

class File:
    _next_file_id = 0
    
    def __init__(self, size, is_free):
        self.size = size
        self.is_free = is_free
        
        if is_free:
            self.id = -1
            return
        
        self.id = File._next_file_id
        File._next_file_id += 1
        
disk_map, expanded_disk_map, disk_map_without_space = [], [], []
checksum, pos = 0, 0

is_free = False
for amount in compressed_disk_map:
    file = File(int(amount), is_free)
    if int(amount) == 0:
        is_free = not is_free
        continue
    
    disk_map.append(file)
    for i in range(int(amount)):
        if is_free:
            expanded_disk_map.append(None)
            continue
            
        expanded_disk_map.append(File._next_file_id - 1)
        disk_map_without_space.append(File._next_file_id - 1)
            
    is_free = not is_free

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

def find_empty_slot_for_file(disk_map, file):
    for i, slot in enumerate(disk_map[:disk_map.index(file)]):
        if slot.is_free and slot.size >= file.size: return slot, i
    return None, 0  

non_empty_files = list(filter(lambda x: not x.is_free, disk_map))
for file in reversed(non_empty_files):
    empty_slot, empty_slot_pos = find_empty_slot_for_file(disk_map, file)
    if not empty_slot: continue
    
    diff = empty_slot.size - file.size

    disk_map.insert(disk_map.index(file), File(file.size, True))
    disk_map.remove(file)

    disk_map.pop(empty_slot_pos)
    if diff > 0:
        if disk_map[empty_slot_pos].is_free: disk_map[empty_slot_pos].size += diff
        else: disk_map.insert(empty_slot_pos, File(diff, True))
    disk_map.insert(empty_slot_pos, file)

checksum, pos = 0, 0
for file in disk_map:
    if file.is_free: 
        pos += file.size
        continue
    
    for i in range(file.size): 
        checksum += (file.id * pos)
        pos += 1
    
print("Answer to part 2:", checksum)