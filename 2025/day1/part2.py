with open('./2025/day1/input.txt', 'r') as file:
    lines = file.readlines()
    
id_list_1 = []
id_list_2 = []

for line in lines:
    ids = line.split(' ', maxsplit=1)
    id_list_1.append(int(ids[0]))
    id_list_2.append(int(ids[1].strip()))

hashmap = {}
for id in id_list_1:
    if id not in hashmap:
        hashmap[id] = 0
        
for id in id_list_2:
    if id in hashmap:
        hashmap[id] += id

total = 0
for value in hashmap.values(): total += value
print(total)