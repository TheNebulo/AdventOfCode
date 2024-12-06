with open('./2024/day1/input.txt', 'r') as file:
    lines = file.readlines()
    
id_list_1 = []
id_list_2 = []

for line in lines:
    ids = line.split(' ', maxsplit=1)
    id_list_1.append(int(ids[0]))
    id_list_2.append(int(ids[1].strip()))
    
def part_1():
    id_list_1.sort()
    id_list_2.sort()

    diff = 0
    for i in range(len(id_list_1)):
        diff += abs(id_list_1[i] - id_list_2[i]) 
        
    return diff

def part_2():
    hashmap = {}
    for id in id_list_1:
        if id not in hashmap:
            hashmap[id] = 0
            
    for id in id_list_2:
        if id in hashmap:
            hashmap[id] += id

    total = 0
    for value in hashmap.values(): total += value
    return total
    
print("Answer to part 1:", part_1())
print("Answer to part 2:", part_2())