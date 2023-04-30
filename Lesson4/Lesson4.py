#Task1
start_with_capital_later = ["john", "marta", "james", "amanda", "marianna"]
print([names.capitalize() for names in start_with_capital_later])

#Task2
list_of_friends = ["John", "Marta", "James", "Amanda", "Marianna"]
text = "NAME"
length = max(len(name) for name in list_of_friends)
center_align = text.center(length, "*")
print(center_align)
for name in list_of_friends:
    print(f'{name.rjust(length)}')

#Task3
import re
camel_case = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []
for i in camel_case:
    words = re.findall(r'[A-Z][a-z0-9]*', i)
    snake_case = '_'.join([word.lower() for word in words])
    snake_case_list.append(snake_case)
print(snake_case_list)

#Task4
languages_dict = {'Python': 'Guido van Rossum', 'Java': 'James Gosling', 'PHP': 'Rasmus Lerdorf',
                  'JavaScript': 'Brendan Eich'}
for language, creator in languages_dict.items():
    print('My favorite programming language is', language, 'it was created by', creator)
del languages_dict["PHP"]
print(languages_dict)

#Task5
e2g = {'stork': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule'}
e2g_new = {'dog': 'hund', 'cat': 'katze'}
print(f'Translation of the word "Owl" from English to German:', e2g['owl'])
e2g_updated = e2g | e2g_new
print('Dictionary:', e2g_updated)
print('German language:', list(e2g_updated.values()))
print('English language:', list(e2g_updated.keys()))

#Task6
subjects_list = []
school_subjects = []
subjects = {
    'science':
        {'physics': ['nuclear physics', 'optics', 'thermodynamics'],
        'computer science': {}, 'biology': {}}
}
for learning_programs in subjects['science']:
    subjects_list.append(learning_programs)
print("Schedule for today:", subjects_list)
for learning_programs in subjects['science']['physics']:
    school_subjects.append(learning_programs)
print("Subjects from physics section:", school_subjects)

#Task7
numbers_dict = {}
for numbers in range(1, 16):
    numbers_dict[numbers] = numbers ** 2
print(numbers_dict)










