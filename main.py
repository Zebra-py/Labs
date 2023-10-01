def _2_or_3(numbers):
    for num in numbers:
        if num == 2 or num == 3:
            return True
    return False

my_list = [1, 4, 3, 5, 7]
result = _2_or_3(my_list)
print(result)