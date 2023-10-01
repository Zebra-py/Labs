def list_to_dict(input_list):
    # Используем генераторное выражение для создания словаря
    result_dict = {index: value for index, value in enumerate(input_list)}
    return result_dict

my_list = ["Книга", "Яблоко", "Олег"]
result = list_to_dict(my_list)
print(result)

# Написать функцию, которая принимает список и с помощью генераторного
# выражения создает и возвращает словарь, где в качестве ключей будут
# номера позиций элементов входящего словаря, а значениями – сами элементы.
