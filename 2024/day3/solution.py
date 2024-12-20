def exec_instruction(instruction):
    numbers = instruction[4:-1].split(',')
    if len(numbers) != 2: return 0
    try:
        if len(numbers[0]) < 1 or len(numbers[0]) > 3: return 0
        if len(numbers[1]) < 1 or len(numbers[1]) > 3: return 0
        num1, num2 = int(numbers[0]), int(numbers[1])
        return num1 * num2
    except:
        return 0
    
with open('./2024/day3/input.txt', 'r') as file:
    memory = ''.join(file.readlines())

total = 0
total_with_exec_toggling = 0
exec_enabled = True

while len(memory) > 0:
    if memory.startswith("do()"):
        exec_enabled = True
        memory = memory[4:]
        continue
    
    if memory.startswith("don't()"):
        exec_enabled = False
        memory = memory[7:]
        continue
    
    if not memory.startswith("mul("):
        memory = memory[1:]
        continue
    
    end_index = memory.find(')')
    if end_index == -1: break
    
    result = exec_instruction(memory[:end_index + 1])
    
    total += result
    if exec_enabled: total_with_exec_toggling += result
    
    memory = memory[5:]
    
print("Answer to part 1:", total)
print("Answer to part 2:", total_with_exec_toggling)