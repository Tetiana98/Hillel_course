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














