import random

def generate():
    random_numbers = []
    for _ in range(6):
        number = random.randint(30, 100)
        random_numbers.append(number)
    return random_numbers
random_numbers = generate()
print(random_numbers)