with open('./2025/day1/input.txt', 'r') as file:
    lines = file.readlines()
    
id_list_1 = []
id_list_2 = []

for line in lines:
    ids = line.split(' ', maxsplit=1)
    id_list_1.append(int(ids[0]))
    id_list_2.append(int(ids[1].strip()))
    
id_list_1.sort()
id_list_2.sort()

diff = 0
for i in range(len(id_list_1)):
    diff += abs(id_list_1[i] - id_list_2[i]) 
    
print(diff)