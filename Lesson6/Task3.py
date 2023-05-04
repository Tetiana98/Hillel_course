#Task3
def is_prime(numbers):
    if numbers < 2 or numbers > 1000:
        return False
    for i in range(2, int(numbers ** 0.5) + 1):
        if numbers % i == 0:
            return False
    return True
