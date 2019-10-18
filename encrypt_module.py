import math
import random


def create_pair():
    a, b, c = [random.randint(1000000, 100000000) for _ in range(3)]
    discriminant = b ** 2 - 4 * a * c

    while discriminant <= 0:
        a, b, c = [random.randint(1000000, 100000000) for _ in range(3)]
        discriminant = b ** 2 - 4 * a * c

    first_part = (-b + math.sqrt(discriminant)) / (2 * a)
    second_part = (-b - math.sqrt(discriminant)) / (2 * a)

    private_key = first_part * second_part
    public_key = (a, b, c)
    print("Successfully created")

    return public_key, private_key
