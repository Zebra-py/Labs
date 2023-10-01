def list_to_dict(input_list):
    # Используем генераторное выражение для создания словаря
    result_dict = {index: value for index, value in enumerate(input_list)}
    return result_dict

my_list = ["Книга", "Яблоко", "Олег"]
result = list_to_dict(my_list)
print(result)
