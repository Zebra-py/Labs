import random

def generate_random_numbers():
    random_numbers = [random.randint(30, 100) for _ in range(6)]
    return random_numbers

result = generate_random_numbers()
print(result)
