#Task2
import math
a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))
D = b ** 2 - 4 * a * c
try:
    if D < 0:
        raise Exception('The discriminant is negative')

    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1 = ", x1)
    print("x2 = ", x2)
except Exception as e:
    print("Error: ", e)

#Task3
while True:
    formula = input('Enter formula: ')
    try:
        values = formula.split()
        if len(values) != 3:
            raise ValueError('Formula must contain 3 elements')
        number_1 = float(values[0])
        number_2 = float(values[2])
        if values[1] not in ['+', '-']:
            raise ValueError('Wrong operator. Only + and - are allowed in this formula ')
        operation = values[1]
    except ValueError as error:
        print(f'Error: {error}')
    else:
        break
if operation == '+':
    result = number_1 + number_2
else:
    result = number_1 - number_2
print(f'Result: {result}')
















