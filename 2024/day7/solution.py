from itertools import product

with open('./2024/day7/input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    
def eval_calculation(num1, operator, num2):
    if operator == '||': return int(str(num1) + str(num2))
    if operator == '*': return num1 * num2
    return num1 + num2
    
def run_all_calculations(numbers, operators, target_result, force_operator=None):
    for combination in product(operators, repeat=len(numbers)-1):
        if force_operator and force_operator not in combination: continue
        result = numbers[0]
        for i in range(len(numbers)-1): result = eval_calculation(result, combination[i], numbers[i+1])
        if result == target_result: return True
    return False

print("This is another brute force solution, and because python, its a bit slow. Please wait a few seconds.")
    
found = 0
found_with_new_operator = 0
for line in lines:
    result, numbers = line.split(':')
    
    result = int(result)
    numbers = [int(number) for number in numbers.strip().split(' ')]
    
    if run_all_calculations(numbers, ['*', '+'], result):  found += result
    elif run_all_calculations(numbers, ['*', '+', '||'], result, force_operator='||'): found_with_new_operator += result   

print("Answer to part 1:", found)
print("Answer to part 2:", found + found_with_new_operator)