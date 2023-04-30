#Task1
C = int(input('Enter "C" '))
F = (C + 32) * 5 / 9
K = C + 273.16
print(f'Kelvin {K}, Fahrenheit {F}')

#Task2
v1 = int(input('Enter liters of first liquids '))
v2 = int(input('Enter liters of second liquids '))
t1 = int(input('Enter temperature of first liquids '))
t2 = int(input('Enter temperature of second liquids '))
if v1 == 0 or v2 == 0:
    print('Liters are not measured in zeros')
elif v1 < 0 or v2 < 0:
    print('Negative numbers in liters measurement cannot be applied')
else:
    v = (v1 * t1 + v2 * t2) / (v1 + v2)
    print(v)

#Task3
UAH = int(input('Enter UAH '))
USD = int(input('Enter USD '))
EUR = int(input('Enter EUR '))
UAH_USD_exchange_rate = 0.027
USD_UAH_exchange_rate = 36.76
UAH_EUR_exchange_rate = 0.025
EUR_UAH_exchange_rate = 40.18
if UAH < 0:
    print('Incorrect input in UAH. Please try again')
elif UAH == 0:
    print('You have zero UAH')
else:
    UahToUsd = UAH * UAH_USD_exchange_rate
    UahToEur = UAH * UAH_EUR_exchange_rate
    print(f'UAH to USD exchange rate is {UahToUsd}')
    print(f'UAH to EUR exchange rate is {UahToEur}')
if USD < 0:
    print('Incorrect input in USD. Please try again')
elif USD == 0:
    print('You have zero USD')
else:
    UsdToUah = USD*USD_UAH_exchange_rate
    print(f'USD to UAH exchange rate is {UsdToUah}')
if EUR < 0:
    print('Incorrect input in EUR. Please try again')
elif EUR == 0:
    print('You have zero EUR')
else:
    EurToUah = EUR*EUR_UAH_exchange_rate
    print(f'EUR to UAH exchange rate is {EurToUah}')

#Task4
number_1 = input('Enter first number ')
number_2 = input('Enter second number ')
operation = input('Choose operation +, - , *, / ')
special_characters_for_operation = '[@_!#$%^&()<>?\|}{~:]abcdefghijklmnopqrstyvwxyz'
special_characters_for_number1_number2 = '[@_!#$%^&()+<>?\/*|}{~:]abcdefghijklmnopqrstyvwxyz'
if any(a in special_characters_for_number1_number2 for a in number_1 and number_2):
    print('You enter special character or letters in to "number_1, number_2"')
elif any(b in special_characters_for_operation for b in operation):
    print('You enter special character or letters in to "operation"')
elif number_2 == 0 and operation == '/':
    print('Zero division is not allowed ')
elif number_1.startswith('-', 0) or number_2.startswith('-', 0):
    number_1 = float(number_1)
    number_2 = float(number_2)
    if operation == '+':
        Sum_1 = number_1 + number_2
        print(f'Sum {Sum_1}')
    elif operation == '-':
        Sum_2 = number_1 - number_2
        print(f'Sum {Sum_2}')
    elif operation == '*':
        Sum_3 = number_1 * number_2
        print(f'Sum {Sum_3}')
    elif operation == '/':
        Sum_4 = number_1 / number_2
        print(f'Sum {Sum_4}')
    else:
        print('Wrong input')
else:
    number_1 = float(number_1)
    number_2 = float(number_2)
    if operation == '+':
        Sum_1 = number_1 + number_2
        print(f'Sum {Sum_1}')
    elif operation == '-':
        Sum_2 = number_1 - number_2
        print(f'Sum {Sum_2}')
    elif operation == '*':
        Sum_3 = number_1 * number_2
        print(f'Sum {Sum_3}')
    elif operation == '/':
        Sum_4 = number_1 / number_2
        print(f'Sum {Sum_4}')
    else:
        print('Wrong input')





















