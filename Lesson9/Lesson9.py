#Task1
import json

with open('group_people.json') as file:
    data = json.load(file)
max_count = 0
group_id = 0
for group in data:
    count = 0
    for person in group['people']:
        if person['gender'] == 'Female' and person['year'] > 1997:
            count += 1
    if count > max_count:
        max_count = count
        group_id = group['id_group']
print('ID of the found group:', group_id)
print('Number of women born after 1977:', max_count)

#Task2
import json

with open('manager_sales.json') as file:
    data = json.load(file)
successful_manager = None
max_total_sales = 0

for manager_data in data:
    amount_sales = sum([car['price'] for car in manager_data['cars']])
    if amount_sales > max_total_sales:
        max_total_sales = amount_sales
        successful_manager = f"{manager_data['manager']['first_name']} {manager_data['manager']['last_name']}"

print(successful_manager, max_total_sales)


