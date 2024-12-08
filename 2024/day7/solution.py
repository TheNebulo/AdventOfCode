from itertools import product
import os

with open('./2024/day7/input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    
def eval_string(num1, operator, num2):
    if operator == '||': return str(num1) + str(num2)
    else: return eval(f"{num1}{operator}{num2}")
    
def eval_strings(numbers):
    results = []
    for combination in product(['*', '+', '||'], repeat=len(numbers)-1):
        result = numbers[0]
        for i in range(len(numbers)-1): result = eval_string(result, combination[i], numbers[i+1])
        results.append(str(result))
    return results
    
found = 0
for line in lines:
    result, numbers = line.split(':')
    numbers = numbers.strip().split(' ')
    
    if result in eval_strings(numbers): found += int(result)
    
print(found)