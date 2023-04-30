#Task1
palindrome_yes_or_not = input('Enter word ')
operation_with_numbers_symbols_impossible = '0123456789[@_!#$%^&()+<>?\/*|}{~:]-'
if any(a in operation_with_numbers_symbols_impossible for a in palindrome_yes_or_not):
    print("Not working with numbers and symbols. Please enter a word")
elif str(palindrome_yes_or_not) == palindrome_yes_or_not[::-1]:
    print("+")
else:
    print("-")

#Task2
text = input('Enter a text ')
search_specific_word = input('Enter the word you want to search ')
if search_specific_word in text:
    print('Yes')
else:
    print("No")

#Task3
enter_string = input('Enter sentence ')
abc_replacement = 'abc'
www_replacement = 'www'
zzz_replacement = 'zzz'
size = len(enter_string)
if enter_string.startswith(abc_replacement, 0):
    change_start = enter_string.replace(abc_replacement, www_replacement)
    print(change_start)
else:
    change_end = enter_string.replace(enter_string[size - 3:], zzz_replacement)
    print(change_end)

#Task4
required_characters_1 = '@'
required_characters_2 = '.'
enter_email = input('Please enter email ')
if required_characters_1 in enter_email and required_characters_2 in enter_email:
    print('YES')
else:
    print('NO')

#Task5
enter_text = input('Enter text ')
string_to_list = enter_text.split()
if len(string_to_list) < 3:
    print(f'The number of elements is less than 3: {len(string_to_list)}')
else:
    print(f'The last 3 items from the list: {string_to_list[-3:]} ')









