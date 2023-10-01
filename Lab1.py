def _2_or_3(numbers):
    for num in numbers:
        # Проверяем, содержится ли 2 или 3 в списке
        if num == 2 or num == 3:
            return True
    # Если после перебора всех элементов не нашли 2 или 3, возвращаем False
    return False

# Пример использования функции:
my_list = [1, 4, 3, 5, 7]
result = _2_or_3(my_list)
print(result)