with open('./2024/day5/input.txt', 'r') as file:
    lines = file.readlines()
    
page_ordering_rules = []
updates = []

page_ordering_loaded = False
for line in lines:
    if line.strip() == '': 
        page_ordering_loaded = True
        continue
    
    if page_ordering_loaded: updates.append(line.strip())
    else: page_ordering_rules.append(line.strip())

page_requirements = {}
for rule in page_ordering_rules:
    required_page, page_to_print = rule.split('|')
    
    if page_to_print not in page_requirements: page_requirements[page_to_print] = []
    page_requirements[page_to_print].append(required_page)

def is_update_ordered(update):
    valid_update = True
    printed_pages = []
    
    for page in update:
        if page not in page_requirements:
            printed_pages.append(page)
            continue
        
        for required_page in page_requirements[page]:
            if required_page not in update: continue
            if required_page not in printed_pages:
                valid_update = False
                break
            
        if not valid_update: break
        printed_pages.append(page)
    
    return valid_update

def order_update(update): # This function should be in the brute force hall of fame
    printed_pages = []
    pages_to_ignore = []
    
    for page in update:
        if page not in page_requirements:
            printed_pages.append(page) 
            continue
        
        for required_page in page_requirements[page]:
            if required_page not in update: continue
            if required_page in pages_to_ignore: continue
            if required_page not in printed_pages:
                pages_to_ignore.append(required_page)
                printed_pages.append(required_page)

        if page not in pages_to_ignore: printed_pages.append(page)
    
    return printed_pages
        

middle_pages_total = 0
middle_pages_for_incorrect = 0
for update in updates:
    update = update.split(',')
    if is_update_ordered(update): middle_pages_total += int(update[len(update) // 2])
    else:
        while not is_update_ordered(update): update = order_update(update) # This is such a dumb line of code
        middle_pages_for_incorrect += int(update[len(update) // 2])
        
print("Answer for part 1:", middle_pages_total)
print("Answer for part 2:", middle_pages_for_incorrect)