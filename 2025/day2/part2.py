def validate_report(report):
    sign = -1 if report[0] - report[1] < 0 else 1
    
    for i in range(len(report) - 1):
        diff = (report[i] - report[i + 1]) * sign
        if diff < 1 or diff > 3: return False
        
    return True

with open('./2025/day2/input.txt', 'r') as file:
    reports = file.readlines()
    
safe = 0
for line in reports:
    report = [int(level) for level in line.strip().split(' ')]
    
    for i in range(len(report)):
        copied_report = report.copy()
        copied_report.pop(i)
        
        if validate_report(copied_report):
            safe += 1
            break
    
print(safe)